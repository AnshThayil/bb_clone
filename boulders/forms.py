from django import forms
from gyms.models import Gym
from walls.models import Wall
from boulders.models import Boulder
from django.shortcuts import get_object_or_404

class BoulderCreateForm(forms.ModelForm):
   
    def __init__(self, *args, gym_pk=None, **kwargs):
        self.gym_pk = gym_pk
        super(BoulderCreateForm, self).__init__(*args, **kwargs)

        # gym = Gym.objects.get(pk = self.gym_pk)
        gym = get_object_or_404(Gym, pk=self.gym_pk)
        self.fields['wall'].queryset = Wall.objects.filter(gym = gym )
    
    class Meta:
        model = Boulder
        fields = ['boulder_name', 'grade' , 'wall']

    boulder_name = forms.CharField()
    grade = forms.IntegerField()
    wall = forms.ModelChoiceField(queryset=None)

class BoulderUpdateForm(forms.ModelForm):

    def __init__(self, *args,gym=None, **kwargs):
        self.gym = gym
        super(BoulderUpdateForm, self).__init__(*args, **kwargs)
        self.fields['wall'].queryset = gym.wall_set.all()
    
    class Meta:
        model = Boulder
        fields = ['boulder_name', 'grade', 'wall']
    
    boulder_name = forms.CharField()
    grade = forms.IntegerField()
    wall = forms.ModelChoiceField(queryset=None)