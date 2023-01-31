from django import forms 
from events import models
#this form for will help with creating new events


class EventForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = "__all__"
         # number_seats and available_seats are missing

class UpdateEventForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = "__all__"