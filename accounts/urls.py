from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('registration/', views.register, name="registration"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('edit/', views.edit, name="edit"),
]