from django.shortcuts import render
from .models import Gym
from boulders.models import Boulder
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.

class GymListView(ListView):
    model = Gym
    context_object_name = 'gyms'

class GymDetailView(DetailView):
    model = Gym
    context_object_name = 'gym'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["boulders"] = Boulder.objects.all().filter(wall__gym = context['gym'])
        return context
    

class GymCreateView(CreateView):
    model = Gym
    fields = ['name', 'addr']

    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super().form_valid(form)