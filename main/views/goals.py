from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json

from main.models import Area, Goal, GoalHistory
from main.forms.goals import GoalForm
from main.forms.goals_history import GoalHistoryForm

class GoalView:
    def update(request, pk):
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

    def delete(request, pk):
        Goal.objects.get(pk = pk).delete()
        return redirect('index')

    def list_one(request, pk):
        goal = get_object_or_404(Goal, pk=pk)
        goal_history = GoalHistory.objects.filter(goal = pk).order_by('-date')
        return render(request, "goal/history.html", {'goal': goal, 'goal_history': goal_history})
