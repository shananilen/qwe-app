from django.contrib import admin
from django.urls import path
from system_user import views

urlpatterns = [
    path('approvals', views.user_approvals, name='approvals_overview_path'),  # approvals
    path('add_group/<str:user_id>', views.approve_user_with_group, name='approve_user_with_group_path'),  # approvals

]
