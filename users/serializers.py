from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # groups = serializers.HyperlinkedRelatedField(view_name='group-detail', read_only=True)
    staff_user =  serializers.SerializerMethodField('get_staff_user')

    def get_staff_user(self, obj):
        return obj.groups.filter(name='StaffUser').exists()

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'staff_user']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name', 'user_set']
