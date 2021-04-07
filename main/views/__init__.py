from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from main.models import Area
from main.forms.goals import GoalForm

class IndexView:
    def index(request):
        areas = Area.objects.all()

        if request.method == "POST":
            form = GoalForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = GoalForm()

        return render(request, "index.html", {'areas': areas, 'form': form})