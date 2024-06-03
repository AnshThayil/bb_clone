from .models import Boulder
from rest_framework import serializers

class BoulderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Boulder
        fields = ['id', 'url', 'boulder_name', 'setter']