from django.urls import path
from .views import BoulderDetailView, BoulderUpdateView, BoulderDeleteView
urlpatterns = [
    path('<int:pk>/', BoulderDetailView.as_view(), name='boulder_detail'),
    path('<int:pk>/update', BoulderUpdateView.as_view(), name='boulder_update'),
    path('<int:pk>/delete', BoulderDeleteView.as_view(), name='boulder_delete'),

]