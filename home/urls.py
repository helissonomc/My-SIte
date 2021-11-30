from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('home/', views.home, name='home'),
    path('', views.home, name='home-empty'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('to-do/', views.todo, name='todo'),
    path('projects/', views.projects, name='projects'),
    path('about/', views.about, name='about'),
]