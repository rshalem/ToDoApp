from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

class ToDoList(models.Model):

    """
    complete field is to notify when a task is completed
    """

    task_title = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='linked_user', on_delete=models.CASCADE)

    def __str__(self):
        return self.task_title

    def get_absolute_url(self):
        return reverse('todoapp:homepage', kwargs={'id': self.id})
