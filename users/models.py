from django.db import models

from django.contrib.auth.models import User
# Create your models here.
from events.models import Event
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    events = models.ManyToManyField(Event)