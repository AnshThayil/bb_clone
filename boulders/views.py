from django.shortcuts import render
from .models import Boulder
from django.views.generic import DetailView

# Create your views here.

class BoulderDetailView(DetailView):
    model = Boulder
    context_object_name = 'boulder'