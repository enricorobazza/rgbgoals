from django import forms
from main.models import GoalHistory
from main.forms.inputs.date import DateInput
from django.forms import HiddenInput

class GoalHistoryForm(forms.ModelForm):
    class Meta:
        model = GoalHistory
        fields = ('goal', 'value')

    def __init__(self, *args, **kwargs):
        super(GoalHistoryForm, self).__init__(*args, **kwargs)
        self.fields["goal"].widget.attrs['react'] = True
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        