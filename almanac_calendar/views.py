from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from .forms import EventForm
from .models import Event

import json

# Create your views here.
def add_event(request):
    if request.POST:
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=201)

        return render(request, 'almanac_calendar/index.html', context={'form': form})
    return render(request, 'almanac_calendar/index.html', context={'form': EventForm()})

def calendar(request):
    events = eval(serializers.serialize("json", Event.objects.all()))
    #print(events[0])
    events = list(map(lambda x: x['fields'], events))
    print(events)
    return render(request, 'almanac_calendar/calendar.html', context={'events': events})

def events_list(request):
    print('in events lists')
    events = Event.objects.all()
    return JsonResponse(list(map(lambda x: model_to_dict(x), events)), safe=False)
