from typing import Collection
from django.db import models
from walls.models import Wall
from django.contrib.auth.models  import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

# Create your models here.
class Boulder(models.Model):
    wall = models.ForeignKey(Wall, on_delete=models.CASCADE)
    boulder_name = models.CharField(max_length=100)
    setter = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['boulder_name', 'wall'], name='unique_boulder_name_per_wall'
            )
        ]

    def __str__(self):
        return self.boulder_name


class Annotation(models.Model):
    boulder = models.ForeignKey(Boulder, on_delete=models.CASCADE)
    coord_x = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    coord_y = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    radius = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"[({self.coord_x}, {self.coord_y}),{self.radius}]"

class Sender(models.Model):
    boulder = models.ForeignKey(Boulder, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.boulder.boulder_name} was sent by {self.sender.first_name}"