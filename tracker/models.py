from django.db import models
from django.utils import timezone


class DailyGoal(models.Model):
    date = models.DateField(default=timezone.localdate, unique=True)
    protein_goal = models.FloatField(default=150)
    calorie_goal = models.FloatField(default=2000)
    carbs_goal = models.FloatField(default=250)
    fats_goal = models.FloatField(default=65)

    def __str__(self):
        return f"Goals for {self.date}"


class FoodEntry(models.Model):
    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]

    name = models.CharField(max_length=200)
    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES, default='snack')
    calories = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    carbs = models.FloatField(default=0)
    fats = models.FloatField(default=0)
    date = models.DateField(default=timezone.localdate)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.meal_type}) — {self.date}"
