from django import forms
from .models import Task
from django.core.exceptions import ValidationError


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'body', ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        if Task.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slag must be unique. We have "{}" slug already'.format(new_slug))

        return new_slug








