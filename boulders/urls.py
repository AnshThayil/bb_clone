from django.urls import path
from .views import BoulderDetailView

urlpatterns = [
    path('<int:pk>/', BoulderDetailView.as_view(), name='boulder-detail')
]