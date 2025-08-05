// Authentication Form Handlers
class AuthHandler {
    constructor() {
        this.initializeNewsletterForm();
        this.initializeLoginForm();
        this.initializeRegistrationForm();
    }

    initializeNewsletterForm() {
        const newsletterForm = document.querySelector('.newsletter-form');
        if (newsletterForm) {
            newsletterForm.addEventListener('submit', (e) => {
                e.preventDefault();
                const email = newsletterForm.querySelector('input[type="email"]').value;
                if (email) {
                    Utils.showToast('Thank you for subscribing!', 'success');
                    newsletterForm.reset();
                } else {
                    Utils.showToast('Please enter a valid email address.', 'warning');
                }
            });
        }
    }

    initializeLoginForm() {
        const loginForm = document.getElementById('login-form');
        if (loginForm) {
            loginForm.addEventListener('submit', (e) => {
                // Add loading state
                const submitBtn = loginForm.querySelector('button[type="submit"]');
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Logging in...';
            });
        }
    }

    initializeRegistrationForm() {
        const regForm = document.getElementById('registration-form');
        if (regForm) {
            regForm.addEventListener('submit', (e) => {
                // Add loading state
                const submitBtn = regForm.querySelector('button[type="submit"]');
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Creating Account...';
            });
        }
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function () {
    new AuthHandler();
});
