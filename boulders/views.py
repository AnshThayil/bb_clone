from .models import Boulder 
from gyms.models import Gym
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .forms import BoulderCreateForm, BoulderUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.shortcuts import get_object_or_404

# Create your views here.

class BoulderDetailView(DetailView):
    model = Boulder
    context_object_name = 'boulder'

class BoulderCreateView(LoginRequiredMixin, CreateView):

    model = Boulder
    # fields = ['boulder_name', 'wall', 'grade']
    form_class = BoulderCreateForm 

    def get_form_kwargs(self):
        kwargs = super(BoulderCreateView, self).get_form_kwargs()
        kwargs['gym_pk'] = self.kwargs['gym_pk']
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(BoulderCreateView, self).get_context_data(**kwargs)
        # context['gym_name'] = Gym.objects.get(pk=self.kwargs["gym_pk"]).name
        gym = get_object_or_404(Gym, pk=self.kwargs["gym_pk"])
        context["gym_name"] = gym.name
        return context
    
    def form_valid(self, form):
        form.instance.setter = self.request.user
        return super().form_valid(form)

class BoulderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Boulder
    form_class = BoulderUpdateForm
    template_name = 'boulders/boulder_update_form.html'

    def get_form_kwargs(self):
        kwargs = super(BoulderUpdateView,self).get_form_kwargs()
        kwargs['gym'] = self.get_object().wall.gym
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super(BoulderUpdateView, self).get_context_data(**kwargs)
        context['gym_name'] = self.get_object().wall.gym.name
        return context

    def form_valid(self, form):
        form.instance.setter = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        boulder = self.get_object()
        if self.request.user == boulder.setter:
            return True
        return False
    
class BoulderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Boulder
    
    def get_success_url(self):
        gym_pk = self.get_object().wall.gym.pk
        return reverse('gym_detail', kwargs={'pk': gym_pk})


    def test_func(self):
        boulder = self.get_object()
        if self.request.user == boulder.setter:
            return True
        return False