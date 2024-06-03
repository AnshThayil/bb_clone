from django.urls import path
from . import views
from .views import GymListView, GymCreateView, GymUpdateView, GymDeleteView, BoulderListView, GymListApi, GymDetailApi
from boulders.views import BoulderCreateView
from walls.views import WallListView, WallCreateView, WallUpdateView, WallDeleteView, WallCreateApi, WallDetailApi

urlpatterns = [
    path('', GymListView.as_view(), name='home'),
    path('gym/<int:pk>', BoulderListView.as_view(), name='gym_detail'),
    path('gym/<int:gym_pk>/create', BoulderCreateView.as_view(), name='boulder_create'),
    path('gym/<int:gym_pk>/walls', WallListView.as_view(), name='wall_list'),
    path('gym/<int:gym_pk>/walls/create', WallCreateView.as_view(), name='wall_create'),
    path('walls/<int:pk>/delete', WallDeleteView.as_view(), name='wall_delete'),
    path('walls/<int:pk>/update', WallUpdateView.as_view(), name='wall_update'),
    path('api/wall', WallCreateApi.as_view(), name='wall-create'),
    path('api/wall/<int:pk>', WallDetailApi.as_view(), name='wall-detail'),
    path('gym/create', GymCreateView.as_view(), name='gym_create'),
    path('gym/<int:pk>/update', GymUpdateView.as_view(), name='gym_update'),
    path('gym/<int:pk>/delete', GymDeleteView.as_view(), name='gym_delete'),
    path('api/gym', GymListApi.as_view(), name='gym-list'), 
    path('api/gym/<int:pk>', GymDetailApi.as_view(), name='gym-detail'),
]
