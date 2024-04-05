from django.db import models
from gyms.models import Gym
from django.urls import reverse

# Create your models here.
class Wall(models.Model):
    '''
    A Django model to represent the Wall object.

    Attributes
    ----
    wall_name: string
        Name of the Wall
    gym: Gym
        Gym associated with the climbing wall
    img_url: Url
        URL where the image is hosted (for simplicity)
    img_width: int
        Image width.
    img_height: int
        Image height.
    '''
    wall_name = models.CharField(max_length=100)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    img_url = models.URLField()
    img_width = models.PositiveIntegerField()
    img_height = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['gym', 'wall_name'], name='unique_wall_name_per_gym'
            )
        ]

    def __str__(self):
        return f"{self.wall_name} at {self.gym.name}"
    
    def get_absolute_url(self):
        return reverse('wall_list', kwargs={'gym_pk': self.gym.pk})