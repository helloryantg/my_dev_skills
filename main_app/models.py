from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    level = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('skill_list')

   
        