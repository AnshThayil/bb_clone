from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gym-home'),
    path('gym/', views.gym, name='gym-detail')
]