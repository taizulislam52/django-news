from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}.')
            return redirect('news-home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})



# user profile
def profile(request):
    return render(request, 'profile.html')