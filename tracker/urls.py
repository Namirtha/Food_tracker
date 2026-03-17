from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_food, name='add_food'),
    path('delete/<int:pk>/', views.delete_entry, name='delete_entry'),
    path('goals/', views.set_goals, name='set_goals'),
    path('history/', views.history, name='history'),
]
