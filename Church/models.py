from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Team(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.name
