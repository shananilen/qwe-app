from django.contrib import admin
from django.urls import path
from user_auth import views

urlpatterns = [
    path('signin', views.user_login, name='login_path'),  # login
    path('signup', views.user_registration, name='signup_path'),  # register
    path('logout', views.user_logout, name='logout_path'),  # logout
    path('', views.landing_dashboard, name='dashboard_path'),  # login
    path('permissions', views.landing_dashboard, name='permission_handle__path'),  # login

]
