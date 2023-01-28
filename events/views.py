from django.shortcuts import render
from django. http import HttpResponse
from .models import Event
# Create your views here.
def get_events (request):
    events = Event.objects.all()
    