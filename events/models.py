from django.db import models
# import this for the dateFiled 
from django.utils import timezone 
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Event(models.Model):
    #this will be the fileds for creating the events by the orginizer
    name= models.CharField(verbose_name="Event name",
    max_length=30 , unique=True , help_text="add name for your event!",default="")
    
    organiser = models.CharField(max_length=30,default="")
    

    date = models.DateField(default= timezone.now)
    image = models.ImageField(upload_to='media')
    # number_seats : models
    # available_seats:

    #don't forget to edit inside model & view ^^^^ 

    def __str__(self) : 
        return f"{self.name} {self.date}"
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="events", default="")