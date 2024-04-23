from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from users.forms import CustomUserCreationForm

User = get_user_model()


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


def profile_role(request, role):
    context = {'role': role}
    return render(request, 'profile.html', context=context)
