from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Sermon(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=100)
    sermon_from = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Team(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Children(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Youth(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title