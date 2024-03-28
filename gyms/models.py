from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Gym(models.Model):
    name = models.CharField(max_length=100)
    addr = models.CharField(max_length=255)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name'], name='unique_gym_name'
            )
        ]

    def __str__(self):
        return self.name



    


