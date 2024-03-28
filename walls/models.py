from django.db import models
from gyms.models import Gym

# Create your models here.
class Wall(models.Model):
    wall_name = models.CharField(max_length=100)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    image_url = models.URLField()
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

