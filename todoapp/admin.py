from django.contrib import admin
from todoapp.models import todoModel


class myToDo(admin.ModelAdmin):
    list_display = ['heading', 'priority', 'category', 'assigned_date', 'due_date', 'done']
    list_filter = ['priority', 'category', 'done']

admin.site.register(todoModel, myToDo)
