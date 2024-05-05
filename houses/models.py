from django.db import models

class House(models.Model):
    name = models.CharField(max_length=150)
    image = models.CharField(max_length=150)
    description = models.TextField()
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
