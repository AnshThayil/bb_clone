from .models import Gym
from rest_framework import serializers
from walls.serializers import WallSerializer
from users.serializers import UserSerializer

class GymSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Gym
        fields = ['id','url', 'name', 'addr', 'staff', 'wall_set']