from .models import Wall
from rest_framework import serializers

class WallSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Wall
        fields = ['id', 'url', 'gym', 'wall_name', 'img_url', 'boulder_set']