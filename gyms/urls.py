from django.urls import path
from . import views
from .views import GymListView, GymDetailView, GymCreateView, GymUpdateView, GymDeleteView, BoulderListView
from boulders.views import BoulderCreateView
from walls.views import WallListView, WallCreateView, WallUpdateView, WallDeleteView

urlpatterns = [
    path('', GymListView.as_view(), name='home'),
    path('gym/<int:pk>', BoulderListView.as_view(), name='gym_detail'),
    path('gym/<int:gym_pk>/create', BoulderCreateView.as_view(), name='boulder_create'),
    path('gym/<int:gym_pk>/walls', WallListView.as_view(), name='wall_list'),
    path('gym/<int:gym_pk>/walls/create', WallCreateView.as_view(), name='wall_create'),
    path('walls/<int:pk>/delete', WallDeleteView.as_view(), name='wall_delete'),
    path('walls/<int:pk>/update', WallUpdateView.as_view(), name='wall_update'),
    path('gym/create', GymCreateView.as_view(), name='gym_create'),
    path('gym/<int:pk>/update', GymUpdateView.as_view(), name='gym_update'),
    path('gym/<int:pk>/delete', GymDeleteView.as_view(), name='gym_delete'),
]
