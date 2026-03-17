from django.contrib import admin
from .models import FoodEntry, DailyGoal


@admin.register(FoodEntry)
class FoodEntryAdmin(admin.ModelAdmin):
    list_display = ['name', 'meal_type', 'calories', 'protein', 'carbs', 'fats', 'date']
    list_filter = ['meal_type', 'date']
    search_fields = ['name']
    date_hierarchy = 'date'


@admin.register(DailyGoal)
class DailyGoalAdmin(admin.ModelAdmin):
    list_display = ['date', 'protein_goal', 'calorie_goal', 'carbs_goal', 'fats_goal']
