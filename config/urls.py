from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from tracker import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from .views import *  # Removed because 'views' is already imported from 'tracker'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-skill/', views.add_skill, name='add_skill'),
    path('pomodoro/', views.pomodoro_session, name='pomodoro'),

    


    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'
    ), name='password_reset_confirm'), # Use your custom logout view
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),
    path('accounts/', include('allauth.urls')),
    path('password_reset/', auth_views.PasswordResetView.as_view(
    template_name='registration/password_reset_form.html'
), name='password_reset'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# If you want to serve static files during development, uncomment the following line:
