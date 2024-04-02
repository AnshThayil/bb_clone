from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Gym(models.Model):
    '''
    A Django model to represent the Gym object.

    Attributes
    ----
    name: string
        Name of the Gym
    address: string
        Address of the Gym
    staff: User
        User associated with the Gym. Only this User can edit gym details and images.
    '''
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


    def get_absolute_url(self):
        return reverse('gym_detail', kwargs={'pk': self.pk})



    


