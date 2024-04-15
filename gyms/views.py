from django.shortcuts import render
from .models import Gym
from boulders.models import Boulder
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from itertools import islice

# Create your views here.

class GymListView(ListView):
    model = Gym
    context_object_name = 'gyms'

class GymDetailView(DetailView):
    model = Gym
    context_object_name = 'gym'

    def boulder_search_generator(self, query, gym):
        for boulder in Boulder.objects.filter(wall__gym = gym, boulder_name__icontains=query).order_by('boulder_name').iterator():
            yield boulder

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query', '')
        pagination = self.request.GET.get('page', '0')
        if query:
            if int(pagination) == 0:
                boulders = self.boulder_search_generator(query, context['gym'])
            else:
                boulders = islice(self.boulder_search_generator(query, context['gym']), (5 * int(pagination)), None)
            
            context['boulders'] = []
            try:
                for _ in range(5):
                    context['boulders'].append(next(boulders))
                context['next_button'] = True
            except StopIteration:
                pass
        else:
            context["boulders"] = Boulder.objects.all().filter(wall__gym = context['gym'])
        return context

class GymCreateView(LoginRequiredMixin, CreateView):
    model = Gym
    fields = ['name', 'addr']

    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super().form_valid(form)

class GymUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Gym
    fields = ['name', 'addr']
    template_name = 'gyms/gym_update_form.html'

    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        gym = self.get_object()
        if self.request.user == gym.staff:
            return True
        return False

class GymDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Gym
    success_url = '/'

    def test_func(self):
        gym = self.get_object()
        if self.request.user == gym.staff:
            return True
        return False
