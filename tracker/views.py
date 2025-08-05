from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from datetime import datetime, timedelta
from .models import UserProfile, Skill, Schedule, Task, RoadmapStep, Badge, Quote, Video, LearningSession, DailyActivity
from .forms import RegistrationForm, SkillForm, ScheduleForm, TaskForm, DailyActivityForm

# User Authentication Views
def register(request):
    """Handle user registration with automatic UserProfile creation."""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, role='student')  # Default role
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to Self-Learning Tracker.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    """Handle user login with error messaging."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')

@login_required
def user_logout(request):
    """Handle user logout with confirmation message."""
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

@login_required
def profile(request):
    """Allow users to edit their profile (bio, role, profile picture)."""
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        bio = request.POST.get('bio')
        role = request.POST.get('role')
        profile_picture = request.FILES.get('profile_picture')
        profile.bio = bio
        profile.role = role
        if profile_picture:
            profile.profile_picture = profile_picture
        profile.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('dashboard')
    return render(request, 'tracker/profile.html', {'profile': profile})

# Dashboard View
@login_required
def dashboard(request):
    """Display user dashboard with skills, tasks, schedules, badges, and daily activities."""
    skills = Skill.objects.filter(user=request.user)
    tasks = Task.objects.filter(user=request.user, completed=False)
    schedules = Schedule.objects.filter(user=request.user, date__gte=datetime.now().date())
    badges = UserBadge.objects.filter(user=request.user)
    quote = Quote.objects.order_by('?').first()  # Random quote
    activities = DailyActivity.objects.filter(user=request.user, date=datetime.now().date())
    
    context = {
        'skills': skills,
        'tasks': tasks,
        'schedules': schedules,
        'badges': badges,
        'quote': quote,
        'activities': activities,
    }
    return render(request, 'tracker/dashboard.html', context)

# Home Page View
def home(request):
    """Render the landing page for all users."""
    return render(request, 'home.html')

# Skill Management Views
@login_required
def add_skill(request):
    """Add a new skill for the user."""
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            messages.success(request, 'Skill added successfully.')
            return redirect('dashboard')
    else:
        form = SkillForm()
    return render(request, 'tracker/add_skill.html', {'form': form})

@login_required
def edit_skill(request, skill_id):
    """Edit an existing skill."""
    skill = Skill.objects.get(id=skill_id, user=request.user)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully.')
            return redirect('dashboard')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'tracker/edit_skill.html', {'form': form})

@login_required
def delete_skill(request, skill_id):
    """Delete a skill with confirmation."""
    skill = Skill.objects.get(id=skill_id, user=request.user)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted successfully.')
        return redirect('dashboard')
    return render(request, 'tracker/confirm_delete.html', {'item': skill, 'type': 'skill'})

# Learning Tracker & Scheduler Views
@login_required
def schedule(request):
    """Create and view daily/weekly schedules."""
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.user = request.user
            schedule.save()
            messages.success(request, 'Schedule created successfully.')
            return redirect('dashboard')
    else:
        form = ScheduleForm()
    schedules = Schedule.objects.filter(user=request.user, date__gte=datetime.now().date())
    return render(request, 'tracker/schedule.html', {'form': form, 'schedules': schedules})

@login_required
def task_list(request):
    """Display and manage user tasks."""
    tasks = Task.objects.filter(user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task added successfully.')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tracker/task_list.html', {'tasks': tasks, 'form': form})

@login_required
def mark_task_complete(request, task_id):
    """Mark a task as completed and award points."""
    task = Task.objects.get(id=task_id, user=request.user)
    task.completed = True
    task.save()
    profile = UserProfile.objects.get(user=request.user)
    profile.points += 10  # Award 10 points for task completion
    profile.save()
    messages.success(request, 'Task marked as completed.')
    return redirect('task_list')

@login_required
def pomodoro_session(request):
    """Handle Pomodoro timer sessions and point allocation."""
    if request.method == 'POST':
        duration = int(request.POST.get('duration', 25))
        skill_id = request.POST.get('skill_id')
        notes = request.POST.get('notes', '')
        skill = Skill.objects.get(id=skill_id, user=request.user) if skill_id else None
        session = LearningSession.objects.create(
            user=request.user,
            skill=skill,
            duration=timedelta(minutes=duration),
            notes=notes
        )
        profile = UserProfile.objects.get(user=request.user)
        points_earned = duration * 2  # 2 points per minute
        profile.points += points_earned
        profile.save()
        # Check for badge eligibility
        check_and_award_badges(request.user, profile.points)
        return JsonResponse({
            'status': 'success',
            'points_earned': points_earned,
            'total_points': profile.points
        })
    skills = Skill.objects.filter(user=request.user)
    return render(request, 'tracker/pomodoro.html', {'skills': skills})

@login_required
def roadmap(request):
    """Display and manage roadmap steps."""
    steps = RoadmapStep.objects.filter(user=request.user)
    if request.method == 'POST':
        skill_id = request.POST.get('skill_id')
        description = request.POST.get('description')
        skill = Skill.objects.get(id=skill_id, user=request.user)
        RoadmapStep.objects.create(user=request.user, skill=skill, description=description)
        messages.success(request, 'Roadmap step added successfully.')
        return redirect('roadmap')
    skills = Skill.objects.filter(user=request.user)
    return render(request, 'tracker/roadmap.html', {'steps': steps, 'skills': skills})

@login_required
def mark_roadmap_step_complete(request, step_id):
    """Mark a roadmap step as completed and award points."""
    step = RoadmapStep.objects.get(id=step_id, user=request.user)
    step.completed = True
    step.save()
    profile = UserProfile.objects.get(user=request.user)
    profile.points += 20  # Award 20 points for step completion
    profile.save()
    messages.success(request, 'Roadmap step marked as completed.')
    return redirect('roadmap')

# Daily Activity Tracker View
@login_required
def daily_activities(request):
    """Manage daily activities (e.g., food, bath, fresh up)."""
    if request.method == 'POST':
        form = DailyActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.save()
            profile = UserProfile.objects.get(user=request.user)
            profile.points += 5  # Award 5 points for activity completion
            profile.save()
            messages.success(request, 'Daily activity added successfully.')
            return redirect('daily_activities')
    else:
        form = DailyActivityForm()
    activities = DailyActivity.objects.filter(user=request.user, date=datetime.now().date())
    return render(request, 'tracker/daily_activities.html', {'form': form, 'activities': activities})

@login_required
def mark_activity_complete(request, activity_id):
    """Mark a daily activity as completed."""
    activity = DailyActivity.objects.get(id=activity_id, user=request.user)
    activity.is_completed = True
    activity.save()
    messages.success(request, 'Activity marked as completed.')
    return redirect('daily_activities')

# Motivation & Analytics Views
@login_required
def motivation(request):
    """Display motivational quotes and videos."""
    quotes = Quote.objects.all()
    videos = Video.objects.all()
    return render(request, 'tracker/motivation.html', {'quotes': quotes, 'videos': videos})

# Leaderboard View
def leaderboard(request):
    """Display top 10 learners based on points."""
    users = UserProfile.objects.order_by('-points')[:10]
    return render(request, 'tracker/leaderboard.html', {'users': users})

# Helper Function for Badge Awards
def check_and_award_badges(user, total_points):
    """Check and award badges based on points."""
    badges = Badge.objects.all()
    for badge in badges:
        if total_points >= badge.points_required and not UserBadge.objects.filter(user=user, badge=badge).exists():
            UserBadge.objects.create(user=user, badge=badge)
            messages.success(user.request, f'Congratulations! You earned the {badge.name} badge.')