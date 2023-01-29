from django.db import models
# import this for the dateFiled 
from django.utils import timezone 
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Event(models.Model):
    #this will be the fileds for creating the events by the orginizer
    event_name= models.CharField(verbose_name="Event name",
    max_length=30 , unique=True , help_text="add name for your event!",default=True)
    
    organizer = models.CharField(max_length=30,default=True)
    event_pic = models.ImageField(upload_to='images',default=True)

    date_and_time = models.DateField(default= timezone.now)
    # totall_seats_num : models
    # booked_seats_num :
    def __str__(self) : 
        return f"{self.event_name} {self.date_and_time}"
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="events", default=True)