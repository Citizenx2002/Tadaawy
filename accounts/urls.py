from os import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from tadaawy import settings
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='signin.html'), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(
        next_page=settings.LOGOUT_REDIRECT_URL), name='signout'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(
        template_name='change-password.html'), name='changepassword'),
    path('changepassword/password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='change-password-done.html'), name='password_change_done'),
    path('about/', views.about, name='about'),
    path('myprofile/', views.profile, name='profile'),
    path('myprofile/profile_edit/', views.profile_edit, name='profile_edit'),
]
