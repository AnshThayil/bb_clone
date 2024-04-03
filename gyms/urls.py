from django.urls import path
from . import views
from .views import GymListView, GymDetailView, GymCreateView

urlpatterns = [
    path('', GymListView.as_view(), name='home'),
    # path('gym/', views.home),
    path('gym/<int:pk>', GymDetailView.as_view(), name='gym_detail'),
    path('gym/create', GymCreateView.as_view(), name='gym_create')
]