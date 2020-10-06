from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class ToDoItem(models.Model):
    PRIORITY_HIGH = 1
    PRIORITY_MEDIUM = 2
    PRIORITY_LOW = 3

    PRIORITY_CHOICES = [(PRIORITY_HIGH, "ВЫСОКИЙ ПРИОРИТЕТ"), (PRIORITY_MEDIUM,"MEDIUM ПРИОРИТЕТ"),(PRIORITY_LOW,"LOW ПРИОРИТЕТ")]



    description = models.CharField(max_length = 64)
    is_completed = models.BooleanField("Completed", default=False)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'tasks')
    # Pole s prioritetami zadachi, mozhno vibirat iz vipadaushego spiska iz lista - PRIORITY CHOICES
    priority = models.IntegerField("Priority", choices = PRIORITY_CHOICES, default=PRIORITY_MEDIUM) 

    def __str__(self):
        return self.description.capitalize()

    def get_absolute_url(self):
        return reverse("tasks:details", args=[self.pk])

    class Meta:
        ordering = ('-created',) #sortirovka po polu created 
    