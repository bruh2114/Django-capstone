from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)

    class Meta:
        app_label = 'band'

class Song(models.Model):
    title = models.CharField(max_length=200)
    duration = models.DurationField()
    released_date = models.DateField()

    class Meta:
        app_label = 'band'

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()

    class Meta:
        app_label = 'band'

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    class Meta:
        app_label = 'band'

class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email