from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
@user_passes_test(lambda user: not user.username, login_url='/profile', redirect_field_name=None)
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account successfully created. Please login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})



# user profile
@login_required
def profile(request):
    return render(request, 'profile.html')