from django import forms
from .models import Task
from django.core.exceptions import ValidationError


class TaskForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField()

    title.widget.attrs.update({'class': 'form-control'})
    body.widget.attrs.update({'class': 'form-control'})

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        return new_slug

    def save(self):
        new_task = Task.objects.create(
            title=self.cleaned_data['title'],
            body=self.cleaned_data['body'])
        return new_task







