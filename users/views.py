from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.urls import reverse

# Create your views here.


def register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for { username }.')
            return redirect('home')
    else:

        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'GET':
        return render(request, 'users/profile.html', context={'profile': Profile.objects.get(user = request.user)})
    if request.method == 'POST':
        obj = Profile.objects.get(user = request.user)
        obj.grade_format_font = not obj.grade_format_font
        obj.save()
        return redirect(reverse('profile'))
