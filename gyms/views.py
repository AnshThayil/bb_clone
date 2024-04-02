from django.shortcuts import render
from .models import Gym
from walls.models import Wall
from boulders.models import Boulder

# Create your views here.


def home(request):
    context = {
        'gyms': Gym.objects.all(),
        'title': 'Gyms'
    }

    return render(request, 'gyms/home.html', context)

def gym(request, pk):
    gym = Gym.objects.get(pk=pk)
    boulders = Boulder.objects.filter(wall__gym = gym)
    
    context = {
        'gym': gym, 
        'title':  gym.name,
        'boulders': boulders,

    }

    return render(request, 'gyms/gym.html', context)