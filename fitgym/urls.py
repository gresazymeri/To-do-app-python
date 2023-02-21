from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Client
    path('', views.home, name='home'),

    # Auth
    path('login/', views.login_user, name='login'),
    path('register', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tasks/create', views.create_task, name='create_task'),
    path('tasks/register', views.register_task, name='register_task'),
    path('tasks/edit/<str:id>', views.edit_task, name='edit_task'),
    path('tasks/update/<str:id>', views.update_task, name='update_task'),
    path('tasks/delete/<str:id>', views.delete_task, name='delete_task'),
    path('task/complete/<str:id>', views.complete_task, name='complete_task'),

    # Custom
    path('error_pages/404/', views.error_404_view, name='error_page'),
]
