from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from main.models import Area, Goal
from main.forms.goals import GoalForm
from main.forms.goals_history import GoalHistoryForm

class Index:
    def index(request):
        areas = Area.objects.all()

        if request.method == "POST":
            form = GoalForm(request.POST)

            if form.is_valid():
                form.save()
        else:
            form = GoalForm()

        return render(request, "index.html", {'areas': areas, 'form': form})

    def update_goal(request, pk):
        if request.method == "POST":
            data = json.loads(request.body.decode('utf-8'))
            data["goal"] = pk
            form = GoalHistoryForm(data)

            if form.is_valid():
                goal_history = form.save()
                goal = Goal.objects.get(pk = goal_history.goal.pk)
                return JsonResponse({'success': True, 'goal': goal.as_dict(request.user)}, safe=False)
            else:
                return JsonResponse({"success": False, "errors": form.errors}, safe=False)
        
        return redirect('index')

    def delete_goal(request, pk):
        Goal.objects.get(pk = pk).delete()
        return redirect('index')