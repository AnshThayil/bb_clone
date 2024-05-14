from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade_format_font = models.BooleanField(default=True)
    points = models.IntegerField()

    def __str__(self):
        return self.user.username
