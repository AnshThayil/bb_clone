from django.shortcuts import render
from .models import Gym

# Create your views here.


def home(request):
    context = {
        'gyms': Gym.objects.all(),
        'title': 'Gyms'
    }

    return render(request, 'gyms/home.html', context)

def gym(request):
    context = {
        'gym': Gym.objects.all().first(),
        'title': 'Replace this'
    }

    return render(request, 'gyms/gym.html', context)