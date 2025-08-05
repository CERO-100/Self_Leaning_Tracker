// Pomodoro Timer Class
class PomodoroTimer {
    constructor() {
        this.duration = 25; // Default 25 minutes
        this.timeLeft = this.duration * 60; // Convert to seconds
        this.isRunning = false;
        this.timer = null;

        this.initializeElements();
        this.bindEvents();
        this.loadDailyStats();
    }

    initializeElements() {
        this.timerDisplay = document.getElementById('timer-display');
        this.progressBar = document.getElementById('progress-bar');
        this.startBtn = document.getElementById('start-btn');
        this.pauseBtn = document.getElementById('pause-btn');
        this.resetBtn = document.getElementById('reset-btn');
        this.durationSelect = document.getElementById('duration-select');
        this.skillSelect = document.getElementById('skill-select');
        this.notesInput = document.getElementById('session-notes');
    }

    bindEvents() {
        this.startBtn.addEventListener('click', () => this.start());
        this.pauseBtn.addEventListener('click', () => this.pause());
        this.resetBtn.addEventListener('click', () => this.reset());
        this.durationSelect.addEventListener('change', (e) => this.setDuration(e.target.value));
    }

    start() {
        if (!this.isRunning) {
            this.isRunning = true;
            this.startBtn.style.display = 'none';
            this.pauseBtn.style.display = 'inline-block';

            this.timer = setInterval(() => {
                this.timeLeft--;
                this.updateDisplay();
                this.updateProgressBar();

                if (this.timeLeft <= 0) {
                    this.complete();
                }
            }, 1000);
        }
    }

    pause() {
        this.isRunning = false;
        clearInterval(this.timer);
        this.startBtn.style.display = 'inline-block';
        this.pauseBtn.style.display = 'none';
    }

    reset() {
        this.pause();
        this.timeLeft = this.duration * 60;
        this.updateDisplay();
        this.updateProgressBar();
    }

    setDuration(minutes) {
        this.duration = parseInt(minutes);
        this.reset();
    }

    updateDisplay() {
        const minutes = Math.floor(this.timeLeft / 60);
        const seconds = this.timeLeft % 60;
        this.timerDisplay.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
    }

    updateProgressBar() {
        const totalSeconds = this.duration * 60;
        const progress = ((totalSeconds - this.timeLeft) / totalSeconds) * 100;
        this.progressBar.style.width = `${progress}%`;
    }

    complete() {
        this.pause();
        this.playCompletionSound();
        this.saveSession();
        this.showCompletionModal();
        this.updateDailyStats();
    }

    saveSession() {
        const formData = new FormData();
        formData.append('duration', this.duration);
        formData.append('skill_id', this.skillSelect.value);
        formData.append('notes', this.notesInput.value);
        formData.append('csrfmiddlewaretoken', Utils.getCookie('csrftoken'));

        fetch('/pomodoro/', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    Utils.showToast(`Session completed! +${data.points_earned} XP`, 'success');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                Utils.showToast('Error saving session', 'danger');
            });
    }

    playCompletionSound() {
        // Play completion sound
        const audio = new Audio('data:audio/wav;base64,UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQoGAACBhYqFbF1fdJivrJBhNjVgodDbq2EcBj+a2/LDciUFLIHO8tiJNwgZaLvt559NEAxQp+PwtmMcBjiR1/LMeSwFJHfH8N2QQAoUXrTp66hVFApGn+DyvmAXIDhd3LGTMAoAPP/5mB');
        audio.play().catch(e => console.log('Audio play failed:', e));
    }

    showCompletionModal() {
        const modal = document.getElementById('completion-modal');
        if (modal) {
            const bootstrapModal = new bootstrap.Modal(modal);
            bootstrapModal.show();
        }
    }

    loadDailyStats() {
        const today = new Date().toDateString();
        const stats = JSON.parse(localStorage.getItem(`pomodoroStats_${today}`)) || {
            sessions: 0,
            focusTime: 0,
            xp: 0
        };
        this.updateStatsDisplay(stats);
    }

    updateDailyStats() {
        const today = new Date().toDateString();
        const stats = JSON.parse(localStorage.getItem(`pomodoroStats_${today}`)) || {
            sessions: 0,
            focusTime: 0,
            xp: 0
        };

        stats.sessions += 1;
        stats.focusTime += this.duration;
        stats.xp += this.duration * 2;

        localStorage.setItem(`pomodoroStats_${today}`, JSON.stringify(stats));
        this.updateStatsDisplay(stats);
    }

    updateStatsDisplay(stats) {
        document.getElementById('sessions-today').textContent = stats.sessions;
        document.getElementById('focus-time-today').textContent = `${stats.focusTime}m`;
        document.getElementById('xp-today').textContent = stats.xp;
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function () {
    if (document.getElementById('timer-display')) {
        new PomodoroTimer();
    }
});
