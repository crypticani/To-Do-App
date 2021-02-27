from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.contrib import messages
from datetime import date


def Lists(request):
    if request.method == 'POST':
        heading = request.POST.get('heading')
        notes = request.POST.get('notes')
        priority = request.POST.get('priority')
        category = request.POST.get('category')
        due_date = request.POST.get('due_date')
        if not due_date:
            due_date = None
        myform = models.todoModel(heading=heading, notes=notes, priority=priority, category=category, due_date=due_date)
        myform.save()
        return HttpResponseRedirect("/")
    else:
        form = models.todoForm
        lists = models.todoModel.objects.order_by("assigned_date")
        return render(request, 'lists.html', {'form': form, 'page_title': 'Lists', 'lists': lists})

def remove(request, item_id): 
    item = models.todoModel.objects.get(id=item_id) 
    item.delete() 
    messages.info(request, "item removed !!!") 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 

def Done(request, item_id):
    item = models.todoModel.objects.get(id=item_id)
    item.done = 'True'
    item.save()
    messages.info(request, "Item mark as done!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def Schedule(request):
    form = models.todoForm
    lists = models.todoModel.objects.order_by("due_date")
    return render(request, 'schedule.html', {'form': form, 'page_title': 'Scheduled Lists', 'lists': lists})

def Today(request):
    form = models.todoForm
    lists = models.todoModel.objects.filter(due_date__date=date.today())
    return render(request, 'today.html', {'form': form, 'page_title': 'Today', 'lists': lists})

