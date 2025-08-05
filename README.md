# Student Progress Tracker – Django Project

A full-featured web application for student skill management, progress tracking, scheduling, daily activities, task management, and motivation—all in one place.

---

## 📦 Project Structure

myproject/
├── config/ # Django project settings, URLs
│ ├── settings.py # Database, static/media configuration, installed apps
│ └── urls.py # Project URL routing
├── tracker/ # Django app
│ ├── models.py # UserProfile, Skill, Schedule, Task, etc.
│ ├── views.py # login, register, dashboard, etc.
│ ├── forms.py # Registration, profile, skill selection
│ ├── templates/
│ │ ├── base.html
│ │ ├── home.html, login.html, ...
│ ├── static/
│ ├── css/ # custom.css
│ ├── js/ # pomodoro.js, chart.js
│ ├── images/ # logo, illustrations, ...
│ └── media/ # user-uploaded files
├── db.sqlite3 # SQLite database (auto created)
└── manage.py # Django management script

## 🚀 Getting Started



---

## 🚀 Key Features

- **Student Registration, Login & Profiles** – Secure user handling with extended profiles and avatars.
- **Skill Tracking** – Define, select, display user skills.
- **Schedules/Tasks** – Add, edit, list daily plans and todo items.
- **Daily Activity Logging** – Keep track of study or work habits.
- **Motivational Quotes** – Random encouragement shown on dashboard.
- **Badges** – Visual awards for milestones achieved.
- **Leaderboards** – Motivate students with gamified ranking.
- **Responsive UI** – Clean templates with Bootstrap and custom CSS; dynamic features with JS.

---

## 🛠️ Setup Instructions

1. **Clone this repo**, then create a virtual environment and install dependencies:
    ```
    python -m venv venv
    source venv/bin/activate
    pip install django
    ```
2. **Migrate the database:**
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

3. **Create a superuser for admin access:**  
    ```
    python manage.py createsuperuser
    ```

4. **Run the development server:**
    ```
    python manage.py runserver
    ```
5. Access the app at `http://127.0.0.1:8000/`

---

## ✅ Typical User Workflow

![Project Workflow Diagram](https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/9f845b25cdcec414acc75e147f734706/6ce289fd-1c40-41c9-b43a-d87705da8482/f912ee2c.png)

### **Workflow Steps**

1. **User Registration / Login:**  
   - New users create an account; returning users sign in.

2. **Dashboard Access:**  
   - View daily tasks, schedule, motivational quotes, earned badges.

3. **Manage Profile and Tasks:**  
   - Update profile info, add skills, add/edit tasks, schedules.
   - Log daily activities for progress tracking.

4. **View Analytics & Leaderboard:**  
   - See stats, completed tasks, top performers, and progress.

5. **Logout:**  
   - End session. User can log in again to return to their dashboard.

---

## 🌟 UI/UX Principles

- **Consistency:** All pages use a common base layout with navigation and footer.
- **Responsiveness:** Mobile, tablet, and desktop-friendly design.
- **Accessibility:** Clean forms, clear calls-to-action.
- **Visual Feedback:** Badges, leaderboards, and progress charts.
- **Engagement:** Motivational quotes and activity tracking gamify the UX.

---

## 📚 Extending & Customizing

- Add new models (like course tracking, messaging)
- Integrate with external APIs (e.g., for quotes, learning materials)
- Enhance with notifications or calendar integrations

---

## 🙋 Support

Have questions? Open an issue or reach out via email. Pull requests welcome for new features or bug fixes! [rettytito@gmail.com](mailto:rettytito@gmail.com) LinkedIn: [LinkedIn](https://www.linkedin.com/in/titoretty/)
---

# DFD (Data Flow Diagram)

# 📊 Data Flow Diagrams (DFD)

Below are detailed DFDs illustrating the operation of the Student Progress Tracker system for your README. You can embed these images directly in your documentation.

---

## **Level 0 DFD: Context Diagram**

Shows core external entities (User/Student, Admin, Database) and the entire system as a black box.

![Level 0 DFD](https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/0af30542761457d3a6c7fedb19a1e907/91a78e09-4867-4274-858e-cd6cdd09258a/b06dabc6.png)

---

## **Level 1 DFD: Main Processes**

Decomposes the system into four major processes: User Management, Task/Schedule Management, Skill & Progress Tracking, and Analytics/Leaderboard, each interfacing with users, the admin, and relevant data stores.

![Level 1 DFD](https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/0af30542761457d3a6c7fedb19a1e907/0475d87e-e1bb-45e1-9872-9e4f2a67b800/f3e86942.png)

---

## **Level 2 DFD: Task & Schedule Management**

Expands the Task/Schedule Management component into sub-processes: Create/Edit Task, Mark Task Complete, Create/Edit Schedule, View & List. Data flows to/from users and the task/schedule data store.

![Level 2 DFD: Tasks & Schedules](https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/0af30542761457d3a6c7fedb19a1e907/835c6e92-fcdf-41e6-8ac5-76035245eeb5/aac5f632.png)

---

## **Level 2 DFD: User Management**

Breaks down User Management into Register User, Login/Authenticate, Edit Profile, Logout—with all data flows and interactions.

![Level 2 DFD: User Management](https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/0af30542761457d3a6c7fedb19a1e907/c13a5166-329f-4d06-af34-6fb1aa037099/556f7827.png)

---

## **Level 2 DFD: Skill & Progress Tracking**

Expands Skill & Progress Tracking into Add Skill, Select/Update Skills, Log Progress, and View Progress, with data flow to the Skill/Progress database.

![Level 2 DFD: Skill & Progress Tracking](https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/0af30542761457d3a6c7fedb19a1e907/3c4aa476-2959-4867-9342-f10eeaecb210/d63209bd.png)

---

> **Tip:** Use these diagrams to communicate the structure and data movement of your Django system with other developers, stakeholders, or for documentation and presentations.

<<<<<<< HEAD
# Student Progress Tracker

A Django-based web application for tracking student progress...
(your local content)
=======
# Self_Leaning_Tracker
(GitHub content - possibly just this line)
>>>>>>> origin/main


