from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Wall
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from gyms.models import  Gym
from django.urls import reverse

# Create your views here.

class WallListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Wall
    context_object_name = 'walls'

    def get_context_data(self, **kwargs):
        context = super(WallListView, self).get_context_data(**kwargs)
        # gym = Gym.objects.get(pk = self.kwargs['gym_pk'])
        gym = get_object_or_404(Gym, pk = self.kwargs['gym_pk'])
        context['walls'] = gym.wall_set.all()
        context['gym'] = gym
        return context
    
    def test_func(self):
        gym = get_object_or_404(Gym, pk=self.kwargs['gym_pk'])
        if self.request.user == gym.staff:
            return True
        return False

class WallCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Wall
    context_object_name = 'wall'
    fields = ['wall_name', 'img_url', 'img_height', 'img_width']

    def form_valid(self, form):
        # form.instance.gym = Gym.objects.get(pk = self.kwargs['gym_pk'])
        form.instance.gym = get_object_or_404(Gym, pk = self.kwargs['gym_pk'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(WallCreateView, self).get_context_data(**kwargs)
        # gym = Gym.objects.get(pk = self.kwargs['gym_pk'])
        gym = get_object_or_404(Gym, pk=self.kwargs['gym_pk'])
        context['gym_name'] = gym.name
        return context
    
    def test_func(self):
        gym = get_object_or_404(Gym, pk = self.kwargs['gym_pk'])
        if self.request.user  == gym.staff:
            return True
        return False

class WallUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Wall
    context_object_name= 'wall'
    fields = ['wall_name', 'img_url', 'img_height', 'img_width']

    def from_valid(self, form):
        form.instance.gym = get_object_or_404(Gym, pk = self.kwargs['gym_pk'])
        return super().form_valide(form)
    
    def get_context_data(self, **kwargs):
        context = super(WallUpdateView, self).get_context_data(**kwargs)
        wall = get_object_or_404(Wall, pk = self.kwargs['pk'])
        context['gym_name'] = wall.gym.name
        return context
    
    def test_func(self):
        wall = self.get_object()
        if self.request.user  == wall.gym.staff:
            return True
        return False

class WallDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Wall

    def get_success_url(self):
        gym_pk = self.get_object().gym.pk
        return reverse('wall_list', kwargs={'gym_pk': gym_pk})

    def test_func(self):
        wall = self.get_object()
        if self.request.user == wall.gym.staff:
            return True
        return False
