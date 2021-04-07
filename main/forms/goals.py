from django import forms
from main.models import Goal
from main.forms.inputs.date import DateInput
from django.forms import HiddenInput

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = '__all__'
        widgets = {
            'due_date': DateInput(format=('%Y-%m-%d')),
            # 'area': HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(GoalForm, self).__init__(*args, **kwargs)
        self.fields["title"].label = "Título"
        self.fields["area"].label = "Área"
        self.fields["value"].label = "Valor da Meta"
        self.fields["value_type"].label = "Tipo do valor"
        self.fields["due_date"].label = "Data de Prazo"
        self.fields["area"].widget.attrs['react'] = True
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        