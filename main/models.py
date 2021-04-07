from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name_plural = "areas"
        db_table = "area"
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def goals(self):
        return Goal.objects.filter(area = self.pk)

    def as_dict(self):
        return {
            'pk': self.pk,
            'name': self.name, 
            'goals': [goal.as_dict() for goal in self.goals],
            'percentage_completed': self.percentage_completed
        }

    @property
    def percentage_completed(self):
        goals = self.goals
        if(len(goals) == 0):
            return 0
        return sum([goal.percentage_completed for goal in goals]) / len(goals)
        

class Goal(models.Model):
    VALUE_TYPES = (('%', 'Porcentagem'), ('F', 'Decimal'), ('I', 'Inteiro'))

    title = models.CharField(max_length=50)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="goal")
    value = models.FloatField()
    value_type = models.CharField(max_length=1, choices=VALUE_TYPES)
    due_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "goals"
        db_table = "goal"
        ordering = ['due_date', 'area', 'title']
    
    def __str__(self):
        return self.title

    def as_dict(self):
        return {
            'pk': self.pk,
            'title': self.title, 
            'area': str(self.area), 
            'value': self.value, 
            'value_type': self.value_type, 
            'due_date': str(self.due_date),
            'percentage_completed': self.percentage_completed,
            'last_value': self.last_value
        }

    @property
    def percentage_completed(self):
        if self.value == 0:
            return 0

        return self.last_value / self.value
    
    @property
    def last_value(self):
        last_history = GoalHistory.objects.filter(goal = self.pk).order_by("-date")
        if(len(last_history) == 0):
            return 0
        return last_history[0].value
        

class GoalHistory(models.Model):
    goal = models.ForeignKey(Goal, related_name="goal_history", on_delete=models.CASCADE)
    value = models.FloatField()
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "goals_history"
        db_table="goal_history"
        ordering = ['date', 'goal']

    def __str__(self):
        return "(" + str(self.date) + ") " + str(self.goal)

class AreaPermission(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="permission")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="area_permission")

    class Meta:
        verbose_name_plural = "areas_permissions"
        db_table="area_permisson"
        ordering = ['area', 'user']
    
    def __str__(self):
        return str(area) + " - " + str(user)

class GoalPermission(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name="permission")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="goal_permission")

    class Meta:
        verbose_name_plural = "goals_permissions"
        db_table="goal_permission"
        ordering = ['goal', 'user']
    
    def __str__(self):
        return str(goal) + " - " + str(user)