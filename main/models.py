from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date, timedelta

# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=20, unique=True)
    icon = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        verbose_name_plural = "areas"
        db_table = "area"
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def goals(self):
        return Goal.objects.filter(area = self.pk)

    def as_dict(self, user=None):
        return {
            'pk': self.pk,
            'name': self.name, 
            'goals': [goal.as_dict(user) for goal in self.goals],
            'percentage_completed': self.percentage_completed,
            'icon': self.icon,
            'has_perm': self.has_perm(user) if user is not None else False
        }

    @property
    def percentage_completed(self):
        goals = self.goals
        if(len(goals) == 0):
            return 0
        return sum([goal.percentage_completed for goal in goals]) / len(goals)

    def has_perm(self, user):
        if user.is_staff:
            return True
        return len(AreaPermission.objects.filter(area = self.pk, user = user.pk)) > 0
        

class Goal(models.Model):
    VALUE_TYPES = (('%', 'Porcentagem'), ('F', 'Decimal'), ('I', 'Inteiro'))
    RECURRENCE_TYPES = ((1, 'Diário'), (7, 'Semanal'), (15, 'Quinzenal'), (30, 'Mensal'), (120, 'Trimestral'), (180, 'Semestral'), (365, 'Anual'))

    title = models.CharField(max_length=50)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="goal")
    value = models.FloatField()
    value_type = models.CharField(max_length=1, choices=VALUE_TYPES)
    start_date = models.DateField(default=timezone.now)
    recurrence = models.IntegerField(choices=RECURRENCE_TYPES)

    class Meta:
        verbose_name_plural = "goals"
        db_table = "goal"
        ordering = ['start_date', 'area', 'title']

    def get_recurrence_display(self):
        for rec in self.RECURRENCE_TYPES:
            value, text = rec
            if value == self.recurrence:
                return text
        return ""

    def get_value_display(self, value):
        if self.value_type == "%":
            return '%d%%'%value
        else:
            return '%d'%int(value)
    
    def __str__(self):
        return self.title

    def as_dict(self, user = None):
        return {
            'pk': self.pk,
            'title': self.title, 
            'area': str(self.area), 
            'value': self.value, 
            'value_display': self.get_value_display(self.value),
            'value_type': self.value_type, 
            'start_date': self.start_date.strftime("%d/%m/%Y"),
            'percentage_completed': self.percentage_completed,
            'last_value': self.last_value,
            'last_value_display': self.get_value_display(self.last_value),
            'has_perm': self.has_perm(user) if user is not None else False,
            'recurrence': self.get_recurrence_display(),
            'history_count': len(self.history)
        }

    @property
    def percentage_completed(self):
        if self.value == 0:
            return 0

        return self.last_value / self.value

    def has_perm(self, user):
        if user.is_staff:
            return True
        if self.area.has_perm(user):
            return True
        return len(GoalPermission.objects.filter(goal = self.pk, user = user.pk)) > 0
    
    @property
    def last_value(self):
        enddate = date.today() + timedelta(days=1)
        startdate = enddate - timedelta(days=self.recurrence)

        last_history = GoalHistory.objects.filter(goal = self.pk, date__range=(startdate, enddate)).order_by("-date")
        if(len(last_history) == 0):
            return 0
        return last_history[0].value

    @property
    def history(self):
        return GoalHistory.objects.filter(goal = self.pk)
        

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

    @property
    def percentage_completed(self):
        if self.goal.value == 0:
            return 0
        return self.value / self.goal.value

    @property
    def value_display(self):
        if self.goal.value_type == "%":
            return '%d%%'%self.value
        else:
            return '%d'%int(self.value)

class AreaPermission(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="permission")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="area_permission")

    class Meta:
        verbose_name_plural = "areas_permissions"
        db_table="area_permisson"
        ordering = ['area', 'user']
        unique_together = (('area', 'user'),)
    
    def __str__(self):
        return str(self.area) + " - " + str(self.user)

class GoalPermission(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name="permission")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="goal_permission")

    class Meta:
        verbose_name_plural = "goals_permissions"
        db_table="goal_permission"
        ordering = ['goal', 'user']
        unique_together = (('goal', 'user'),)
    
    def __str__(self):
        return str(self.goal) + " - " + str(self.user)