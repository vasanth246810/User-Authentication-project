from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import render, redirect
from .forms import SignupForm, SigninForm
from .models import UserProfile

def signup_view(request):
    if request.session.get('user_id'):
        return redirect('dashboard')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            UserProfile.objects.create(user=user.username,first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],email=form.cleaned_data['email'])           
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['signup_timestamp'] = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
            request.session['user_type'] = 'new_user'
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'Userapp/signup.html', {'form': form})



def signin_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                request.session['login_timestamp'] = timezone.now().strftime("%Y-%m-%d %H:%M")
                messages.success(request, f'Welcome back, {user.first_name or user.username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SigninForm()
    return render(request, 'Userapp/signin.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'Userapp/dashboard.html')

def logout_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        # Clear all session data
        request.session.flush()
        logout(request)
        messages.success(request, f'Goodbye {username}! You have been logged out successfully.')
    return redirect('signin')