from django.contrib import admin
from main.models import *

models = [Area, Goal, GoalHistory, AreaPermission, GoalPermission]

for model in models:
    admin.site.register(model)


# Register your models here.
