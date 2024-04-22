from django.urls import path
from .views import BoulderDetailView, BoulderUpdateView, BoulderDeleteView, SenderDeleteView, SenderCreateView
urlpatterns = [
    path('<int:pk>/', BoulderDetailView.as_view(), name='boulder_detail'),
    path('<int:pk>/update', BoulderUpdateView.as_view(), name='boulder_update'),
    path('<int:pk>/delete', BoulderDeleteView.as_view(), name='boulder_delete'),
    path('<int:gym_pk>/deletesend/<int:pk>', SenderDeleteView.as_view(), name='sender_delete'),
    path('<int:pk>/createsend', SenderCreateView.as_view(), name='sender_create')

]
