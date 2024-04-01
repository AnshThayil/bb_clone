from django.shortcuts import render
from .models import Boulder

# Create your views here.
def boulder(request, pk):
    boulder = Boulder.objects.get(pk=pk)
    context = {
        'boulder': boulder,
        'annotations': boulder.annotation_set.all()
    }

    return render(request, 'boulders/boulder.html', context)