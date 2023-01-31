from django.shortcuts import render , redirect
from django. http import HttpResponse
from .models import Event
from events.forms import EventForm ,UpdateEventForm

# Create your views here.
def get_events (request):
    events = Event.objects.all() # pass all the objects inside the events
    occisions =[] #created empty list
    for event in events: # for the one event 
        occisions.append({ # add the objects inside the new array 
            'name':event.name ,
            'id':event.id, # we pass the id of the events
            'image':event.image,
            'Organiser':event.organiser,
            # 'number of seats':event.number_seats,
            # 'available seats':event.available_seats,  
            }
        )
    context = { # this will be sent to the html 
        'events':occisions
    }

    return render (request, 'event_list.html', context)
    


def events_area (request, id):
    eventArea = Event.objects.get(id=id) # pass all the objects inside the events
    
    context = { # this will be sent to the html 
        'eventArea':eventArea
    }

    return render (request,'booking.html', context)


def create_events(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST,request.FILES)#we want the user to ba able to add pic
        if form.is_valid():
            form.save()
            return redirect ('events')


    context ={
        "form" : form,
    }
    return render(request, 'create_event.html' ,context)



def update_events(request, id):
    event_item = Event.objects.get(id=id)
    form = UpdateEventForm(instance=event_item)

    if request.method == "POST":
        form = UpdateEventForm(request.POST,instance=event_item)
        if form.is_valid():
            form.save()
            return redirect('events')
    context = {
        'form' : form,
        'event_item': event_item
    }
    return render(request, 'update_event.html' , context)

