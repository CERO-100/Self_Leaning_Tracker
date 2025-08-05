from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

# User Profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[
        ('student', 'Student'), 
        ('mentor', 'Mentor'), 
        ('professional', 'Professional')
    ])
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    points = models.IntegerField(default=0)  # For leaderboard and badges

    def __str__(self):
        return self.user.username

# Skill
class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True)
    level = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ])
    progress = models.IntegerField(default=0)
    category = models.CharField(max_length=50, choices=[
        ('programming', 'Programming'),
        ('soft_skills', 'Soft Skills'),
        ('management', 'Management')
    ])

    def __str__(self):
        return self.name

# UserSkill (Intermediate Table for User-Skill Relationship)
class UserSkill(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency_level = models.IntegerField(default=1)
    time_spent = models.DurationField(default=timedelta(0))

    def __str__(self):
        return f"{self.userprofile.user.username} - {self.skill.name}"

# Schedule
class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    task = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.date} - {self.time}: {self.task}"

# Task
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    priority = models.CharField(max_length=10, choices=[
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low')
    ])
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# LearningSession
class LearningSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True)
    duration = models.DurationField()
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.skill.name if self.skill else 'No Skill'} ({self.duration})"

# RoadmapStep
class RoadmapStep(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description

# Badge
class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    points_required = models.IntegerField()

    def __str__(self):
        return self.name

# UserBadge
class UserBadge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    earned_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.badge.name}"

# Quote
class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"\"{self.text[:50]}...\" - {self.author}"

# Video
class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.title

# DailyActivity
class DailyActivity(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('personal_care', 'Personal Care'),
        ('other', 'Other')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    time_of_day = models.TimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title