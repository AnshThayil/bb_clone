from collections.abc import Sequence
from django.shortcuts import render
from .models import Gym
from boulders.models import Boulder
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from itertools import islice
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission, SAFE_METHODS
from .serializers import GymSerializer

# Create your views here.

class GymListView(ListView):
    model = Gym
    context_object_name = 'gyms'
    paginate_by = 4

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'name')
        return ordering
    
    def get_queryset(self):
        ordering = self.get_ordering()
        gyms = Gym.objects.all().order_by(ordering)
        query = self.request.GET.get('query', '')
        if query:
            gyms = gyms.filter(name__icontains=query).order_by(ordering)
        return gyms
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ordering'] = self.get_ordering()
        query  = self.request.GET.get('query', '')
        if query:
            context['query'] = query
        return context

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

class BoulderListView(ListView):
    model = Boulder
    # template_name = 'gyms/boulder_list.html'
    context_object_name = 'boulders'
    paginate_by = 5

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'boulder_name')
        return ordering

    def get_queryset(self):
        ordering = self.get_ordering()
        boulders = Boulder.objects.all().filter(wall__gym__pk = self.kwargs['pk']).order_by(ordering)
        query = self.request.GET.get('query', '')
        if query != '':
            boulders = boulders.filter(boulder_name__icontains = query).order_by(ordering)
        return boulders
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['gym'] = Gym.objects.get(pk = self.kwargs['pk'])
        context['ordering'] = self.get_ordering()
        query = self.request.GET.get('query', '')
        if query:
            context['query'] = query
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

class GymStaffOrReadOnly(BasePermission): 
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.staff == request.user

class IsStaffUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.groups.filter(name='StaffUser').exists()

class GymListApi(generics.ListCreateAPIView):
    permission_classes = [IsStaffUserOrReadOnly]
    queryset = Gym.objects.all()
    serializer_class = GymSerializer

class GymDetailApi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [GymStaffOrReadOnly]
    queryset = Gym.objects.all()
    serializer_class = GymSerializer