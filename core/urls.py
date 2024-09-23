from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('sprints/', views.sprint_list, name='sprint_list'),
    path('sprints/<int:pk>/', views.sprint_detail, name='sprint_detail'),
    path('sprints/create/', views.sprint_create, name='sprint_create'),

]