📚 Self-Learning Tracker
A web-based application built with Django, HTML, CSS, JavaScript, Bootstrap, and Tailwind CSS to help students, job seekers, professionals, and self-learners track, organize, and stay motivated in their learning journey.

🚀 Features
Core Features
✅ User Authentication – Register, login, and manage your account securely.

✅ Skill Management – Add, edit, and track your learning skills (soft skills, programming, management, etc.).

✅ Scheduling & Timers – Plan your daily/weekly study sessions and track time spent.

✅ Progress Tracking – View your learning progress and milestones.

✅ Motivational Section – Daily quotes, challenges, and achievements.

✅ To-Do List – Priority-based task management (Notion-inspired).

✅ Analytics – Visual charts of your study hours and progress.

✅ Responsive Design – Mobile, tablet, and desktop-friendly.

🛠️ Tech Stack
Technology	Purpose
Python (Django)	Backend framework
SQLite / MySQL	Database
HTML, CSS, JS	Frontend structure & interactivity
Bootstrap / Tailwind CSS	Styling & responsive design
Chart.js	Data visualization

📂 Project Structure
csharp
Copy
Edit
self_learning_tracker/
│
├── tracker/                  # Main app
│   ├── migrations/           # Database migrations
│   ├── static/               # Static files (CSS, JS, Images)
│   ├── templates/            # HTML templates
│   ├── models.py              # Database models
│   ├── views.py               # Business logic
│   ├── urls.py                # App URLs
│
├── self_learning_tracker/     # Project configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # Root URLs
│
├── manage.py                  # Django CLI tool
└── README.md                  # Project documentation
⚙️ Installation & Setup
1️⃣ Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/self-learning-tracker.git
cd self-learning-tracker
2️⃣ Create and activate a virtual environment
bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
3️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
5️⃣ Start the server
bash
Copy
Edit
python manage.py runserver
Now visit http://127.0.0.1:8000/ in your browser 🎉

📊 Screenshots
Feature	Screenshot
databse
<img width="1874" height="868" alt="image" src="https://github.com/user-attachments/assets/72f10c59-5975-4dea-a2ff-9ee28c1999fa" />
base.html


🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📜 License
This project is licensed under the MIT License – see the LICENSE file for details.
