from django import template
from django.utils.safestring import mark_safe
import locale
import json

register = template.Library()

@register.filter
def form_as_json(form):
    form_list = []
    for key in form.fields.keys():
        field = {}
        field["id"] = key
        field["type"] = form.fields[key].widget.input_type
        form_list.append(field)

    return json.dumps(form_list)

@register.filter
def queryset_as_json(queryset, user=None):
    return json.dumps([elem.as_dict(user) for elem in queryset])

@register.filter
def render_in_react(field):
    return 'react' in field.field.widget.attrs and field.field.widget.attrs['react'] == True

@register.filter
def format_percentage(percentage):
    return "%d%%"%int(percentage*100)

