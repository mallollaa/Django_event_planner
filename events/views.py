from django.shortcuts import render
from django. http import HttpResponse
from .models import Event
# Create your views here.
def get_events (request):
    events = Event.objects.all() # pass all the objects inside the events
    occisions =[] #created empty list
    for event in events: # for the one event 
        occisions.append({ # add the objects inside the new array 
            'name':event.name ,
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
    


