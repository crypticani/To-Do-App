from django.db import models
from django.forms import ModelForm
from django.forms import DateTimeInput,TextInput, Textarea, TimeInput
from datetime import datetime, date
from django import forms


class todoModel(models.Model):
    heading = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    p = (('None', 'None'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'))
    c = (('Personal', 'Personal'), ('Work', 'Work'), ('Other', 'Other'))
    priority = models.CharField(choices=p, default='None', blank=True, max_length=10)
    category = models.CharField(choices=c, default='Other', blank=True, max_length=10)
    assigned_date = models.DateTimeField(default=datetime.now, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False, blank=True)

    class Meta:
        managed = True


    def __str__(self):
        return self.heading 


class todoForm(ModelForm):
    class Meta:
        model = todoModel
        fields = ('heading', 'notes', 'priority', 'category', 'due_date')
        widgets = {
            'due_date': DateTimeInput(attrs={'type': 'date'}),
            'heading': TextInput(attrs={'size': '30'}),
            'notes': Textarea(attrs={'rows':4, 'cols':30}),
        }