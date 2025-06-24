from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .forms import SignupForm, SigninForm
from .models import UserProfile
import hashlib

def signup_view(request):
    try:
        if request.user.is_authenticated:
            return redirect('dashboard')
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                UserForm = form.save(commit=False)
                UserForm.password = Hashpassword(form.cleaned_data['password'])
                print("UserForm.password:", UserForm.password)
                UserForm.save()
                request.session['user_id'] = UserForm.id
                request.session['username'] = UserForm.user
                request.session['signup_timestamp'] = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
                return redirect('dashboard')
            else:
                form = SignupForm()
    except Exception as e:
        messages.error(request, f"Signup failed: {str(e)}")
        form = SignupForm()
    return render(request, 'Userapp/signup.html', {'form': form})

def signin_view(request):
    try:
        if request.session.get('user_id'):
            return redirect('dashboard')
        if request.method == 'POST':
            form = SigninForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = UserProfile.objects.filter(user=username).first()
                if user:
                    if user.password == Hashpassword(password):
                        request.session['login_timestamp'] = timezone.now().strftime("%Y-%m-%d %H:%M")
                        request.session['username'] = username
                        messages.success(request, f'Welcome back, {user.user}!')
                        return redirect('dashboard')
                    else:
                        messages.error(request, 'Invalid username or password.')
        else:
            form = SigninForm()
    except Exception as e:
        messages.error(request, f"Sign in failed: {str(e)}")
        form = SigninForm()
    return render(request, 'Userapp/signin.html', {'form': form})

def dashboard_view(request):
    try:
        UserInfo = UserProfile.objects.filter(user=request.session.get('username')).first()
        return render(request, 'Userapp/dashboard.html', {'user': UserInfo})
    except Exception as e:
        messages.error(request, f"Dashboard error: {str(e)}")
    return redirect('signin')

def logout_view(request):
    try:
        if request.session.get('user_id'):
            username = request.session['username']
            request.session.flush()
            messages.success(request, f'Goodbye {username}! You have been logged out successfully.')
    except Exception as e:
        messages.error(request, f"Logout failed: {str(e)}")
    return redirect('signin')

def Hashpassword(password):
    s = '5gz'
    pwd_salt = password + s
    hashed = hashlib.sha256(pwd_salt.encode()).hexdigest()
    return hashed