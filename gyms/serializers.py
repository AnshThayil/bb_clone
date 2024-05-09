from .models import Gym
from rest_framework import serializers

class GymSerializer(serializers.ModelSerializer):
    
    staff = serializers.HyperlinkedRelatedField(view_name='user-detail', format='html', read_only=True)
    # wall_set = serializers.HyperlinkedRelatedField(view_name='wall_update', format='html', read_only=True)

    class Meta:
        model = Gym
        fields = ['url', 'name', 'addr', 'staff', 'wall_set']