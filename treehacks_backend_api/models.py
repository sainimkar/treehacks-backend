from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    imgUrl = models.CharField(max_length = 500)

    def __str__(self):
        return self.task

class PhotoResponse(models.Model):

    status = models.CharField(max_length= 50)
    imgUrl = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.task

