from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.db.models import Sum
from datetime import timedelta
from .models import FoodEntry, DailyGoal
from .forms import FoodEntryForm, DailyGoalForm


def dashboard(request):
    today = timezone.localdate()
    entries = FoodEntry.objects.filter(date=today)

    # Get or create today's goals
    goal, _ = DailyGoal.objects.get_or_create(date=today, defaults={
        'protein_goal': 150, 'calorie_goal': 2000,
        'carbs_goal': 250, 'fats_goal': 65,
    })

    # Daily totals
    totals = entries.aggregate(
        total_calories=Sum('calories'),
        total_protein=Sum('protein'),
        total_carbs=Sum('carbs'),
        total_fats=Sum('fats'),
    )
    total_calories = totals['total_calories'] or 0
    total_protein  = totals['total_protein']  or 0
    total_carbs    = totals['total_carbs']    or 0
    total_fats     = totals['total_fats']     or 0

    def pct(val, goal_val):
        return min(round((val / goal_val) * 100) if goal_val else 0, 100)

    # Group entries by meal type
    meals = {}
    for choice_key, choice_label in FoodEntry.MEAL_CHOICES:
        meal_entries = entries.filter(meal_type=choice_key)
        if meal_entries.exists():
            meals[choice_label] = meal_entries

    context = {
        'today': today,
        'entries': entries,
        'meals': meals,
        'goal': goal,
        'total_calories': round(total_calories, 1),
        'total_protein':  round(total_protein, 1),
        'total_carbs':    round(total_carbs, 1),
        'total_fats':     round(total_fats, 1),
        'pct_calories': pct(total_calories, goal.calorie_goal),
        'pct_protein':  pct(total_protein,  goal.protein_goal),
        'pct_carbs':    pct(total_carbs,    goal.carbs_goal),
        'pct_fats':     pct(total_fats,     goal.fats_goal),
    }
    return render(request, 'tracker/dashboard.html', context)


def add_food(request):
    if request.method == 'POST':
        form = FoodEntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{form.cleaned_data["name"]}" added successfully!')
            return redirect('dashboard')
    else:
        form = FoodEntryForm(initial={'date': timezone.localdate()})
    return render(request, 'tracker/add_food.html', {'form': form})


def delete_entry(request, pk):
    entry = get_object_or_404(FoodEntry, pk=pk)
    if request.method == 'POST':
        name = entry.name
        entry.delete()
        messages.success(request, f'"{name}" removed.')
    return redirect('dashboard')


def set_goals(request):
    today = timezone.localdate()
    goal, _ = DailyGoal.objects.get_or_create(date=today, defaults={
        'protein_goal': 150, 'calorie_goal': 2000,
        'carbs_goal': 250, 'fats_goal': 65,
    })
    if request.method == 'POST':
        form = DailyGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Goals updated!')
            return redirect('dashboard')
    else:
        form = DailyGoalForm(instance=goal)
    return render(request, 'tracker/set_goals.html', {'form': form, 'goal': goal})


def history(request):
    today = timezone.localdate()
    # Last 7 days
    days = []
    for i in range(7):
        day = today - timedelta(days=i)
        entries = FoodEntry.objects.filter(date=day)
        totals = entries.aggregate(
            cal=Sum('calories'), pro=Sum('protein'),
            carb=Sum('carbs'), fat=Sum('fats'),
        )
        try:
            goal = DailyGoal.objects.get(date=day)
        except DailyGoal.DoesNotExist:
            goal = None
        days.append({
            'date': day,
            'entries': entries,
            'calories': round(totals['cal'] or 0, 1),
            'protein':  round(totals['pro'] or 0, 1),
            'carbs':    round(totals['carb'] or 0, 1),
            'fats':     round(totals['fat'] or 0, 1),
            'goal': goal,
        })
    return render(request, 'tracker/history.html', {'days': days})
