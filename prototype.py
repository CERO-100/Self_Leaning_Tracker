import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import json
import io

# --- Page Configuration ---
st.set_page_config(
    page_title="Self-Learning Tracker Prototype",
    page_icon="🎯",
    layout="wide"
)

# --- Custom CSS ---
st.markdown("""
<style>
.main-header {background: linear-gradient(135deg,#2A9D8F,#6D6875);padding:2rem;border-radius:10px;color:white;text-align:center;margin-bottom:2rem;}
.metric-card {background:#f8f9fa;padding:1rem;border-radius:8px;border-left:4px solid #2A9D8F;margin:0.5rem 0;}
.activity-card {background:#e8f5f3;padding:1rem;border-radius:8px;margin:0.5rem 0;}
.pomodoro-display {font-size:4rem;font-weight:bold;text-align:center;color:#2A9D8F;background:#f8f9fa;padding:2rem;border-radius:20px;margin:1rem 0;}
</style>
""", unsafe_allow_html=True)

# --- Session State Initialization ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'profile' not in st.session_state:
    st.session_state.profile = {
        'xp': 200, 'level': 4, 'streak': 5,
        'sessions': 30, 'hours': 18,
        'skills': ['Programming', 'Design', 'Soft Skills'],
        'activities': []
    }
if 'pomodoro' not in st.session_state:
    st.session_state.pomodoro = {'running': False, 'skill': None, 'duration': 25, 'time_left': 1500}
if 'notifications' not in st.session_state:
    st.session_state.notifications = []

# --- Authentication ---
def login_page():
    st.markdown('<div class="main-header"><h1>🎯 Self-Learning Tracker</h1></div>', unsafe_allow_html=True)
    if st.button("🔐 Login with Google"):
        st.session_state.logged_in = True
        st.session_state.username = "Tito Retty"
        st.success("Logged in as Tito Retty")
    st.markdown("---")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username and password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome, {username}")
        else:
            st.error("Enter both fields")

# --- Daily Activity Tracker ---
def daily_activities():
    st.subheader("🗓 Daily Activity Tracker")
    date = st.date_input("Date", datetime.today())
    name = st.text_input("Activity Name", "")
    category = st.selectbox("Category", ["Food", "Hygiene", "Exercise", "Other"])
    if st.button("Add Activity"):
        st.session_state.profile['activities'].append({'date': str(date), 'name': name, 'category': category})
        st.success("Activity logged")
    # Display
    df_act = pd.DataFrame(st.session_state.profile['activities'])
    if not df_act.empty:
        st.dataframe(df_act)

# --- Pomodoro Timer ---
def pomodoro_page():
    st.subheader("🍅 Pomodoro Timer")
    pom = st.session_state.pomodoro
    # Controls
    pom['skill'] = st.selectbox("Skill", pom['skill'] or [""] + st.session_state.profile['skills'])
    duration = st.select_slider("Duration (minutes)", [15,25,30,45], value=pom['duration'])
    if duration != pom['duration']:
        pom.update({'duration': duration, 'time_left': duration * 60})
    # Timer display
    if pom['running']:
        mins, secs = divmod(pom['time_left'], 60)
        st.markdown(f"<div class='pomodoro-display'>{mins:02d}:{secs:02d}</div>", unsafe_allow_html=True)
        pom['time_left'] -= 1
        if pom['time_left'] <= 0:
            pom['running'] = False
            reward = pom['duration'] * 2
            st.session_state.profile['xp'] += reward
            st.balloons(); st.success(f"Session complete! +{reward} XP")
    else:
        st.markdown(f"<div class='pomodoro-display'>{pom['duration']:02d}:00</div>", unsafe_allow_html=True)
    # Buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("▶️ Start") and pom['skill']:
            pom['running'] = True
    with col2:
        if st.button("⏸️ Pause"):
            pom['running'] = False
    with col3:
        if st.button("🔄 Reset"):
            pom.update({'running': False, 'time_left': pom['duration']*60})

# --- Analytics ---
def analytics_page():
    st.subheader("📊 Progress Analytics")
    # Sample data
    dates = pd.date_range(end=datetime.today(), periods=7).strftime("%Y-%m-%d")
    xp = [100,80,120,90,70,150,110]
    df = pd.DataFrame({'date':dates,'xp':xp})
    fig = px.line(df, x='date', y='xp', title="Last 7 Days XP", markers=True)
    st.plotly_chart(fig)

# --- Skills Management ---
def skills_page():
    st.subheader("🎯 Skills Management")
    for skill in st.session_state.profile['skills']:
        st.markdown(f"- {skill}")
    new_skill = st.text_input("Add New Skill", "")
    if st.button("Add Skill") and new_skill:
        st.session_state.profile['skills'].append(new_skill)
        st.success(f"Added {new_skill}")

# --- Achievements & Leaderboard ---
def achievements_page():
    st.subheader("🏆 Achievements & Leaderboard")
    st.markdown("**Current XP:** " + str(st.session_state.profile['xp']))
    leaderboard = pd.DataFrame([
        {'rank':1,'user':'Jane Doe','xp':st.session_state.profile['xp']},
        {'rank':2,'user':'Alice','xp':300},
        {'rank':3,'user':'Bob','xp':250},
    ])
    st.table(leaderboard)

# --- Smart Notifications (Simulated) ---
def notify(message, category="info"):
    st.session_state.notifications.append((message, category))

def notifications_widget():
    if st.session_state.notifications:
        st.subheader("🔔 Notifications")
        for msg, cat in st.session_state.notifications:
            st.info(msg) if cat=="info" else st.error(msg)

# --- Offline Mode Stub & Data Export ---
def export_data():
    st.subheader("📥 Export Data")
    data = json.dumps(st.session_state.profile)
    buf = io.StringIO(data)
    json_data = json.dumps(data)
    st.download_button("Download Profile JSON", data=json_data, file_name="profile.json")






# --- Main App ---
def main_app():
    st.markdown(f"<div class='main-header'><h1>Welcome, {st.session_state.username}</h1></div>", unsafe_allow_html=True)
    notifications_widget()
    page = st.sidebar.selectbox("Go to", ["Dashboard","Daily Activities","Pomodoro","Analytics","Skills","Achievements"])
    if page=="Dashboard":
        st.subheader("🏠 Dashboard")
        st.markdown(f"- XP: {st.session_state.profile['xp']}")
        st.markdown(f"- Level: {st.session_state.profile['level']}")
        st.markdown(f"- Streak: {st.session_state.profile['streak']} days")
    elif page=="Daily Activities":
        daily_activities()
    elif page=="Pomodoro":
        pomodoro_page()
    elif page=="Analytics":
        analytics_page()
    elif page=="Skills":
        skills_page()
    elif page=="Achievements":
        achievements_page()
    export_data()

# --- Run ---
if not st.session_state.logged_in:
    login_page()
else:
    main_app()
