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
def queryset_as_json(queryset):
    return json.dumps([elem.as_dict() for elem in queryset])

@register.filter
def render_in_react(field):
    return 'react' in field.field.widget.attrs and field.field.widget.attrs['react'] == True

