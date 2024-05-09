from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.urls import reverse
from django.contrib.auth.models import Group, User
from rest_framework import generics
from .serializers import UserSerializer, GroupSerializer

# Create your views here.


def register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            staff_group = get_object_or_404(Group, name='StaffUser')
            user_group = get_object_or_404(Group, name='EndUser')
            username = form.cleaned_data.get('username')
            user = get_object_or_404(User, username=username)
            if (form.cleaned_data.get('staff_user')):
                staff_group.user_set.add(user)
            user_group.user_set.add(user)
            messages.success(request, f'Account created for { username }.')
            return redirect('home')
    else:

        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'GET':
        return render(request, 'users/profile.html', context={'profile': Profile.objects.get(user = request.user), 'ascents': request.user.sender_set.all().order_by('-date')})
    if request.method == 'POST':
        obj = Profile.objects.get(user = request.user)
        obj.grade_format_font = not obj.grade_format_font
        obj.save()
        return redirect(reverse('profile'))

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetail(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
