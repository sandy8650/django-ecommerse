from django.shortcuts import redirect, render
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)   
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successful')
            return redirect('accounts:login')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }   
    return render(request, 'accounts/register.html', context)


def loginView(request):
    form = LoginForm()
    try:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in.')
                return redirect('products:home')
        else:
            
            messages.error(request, 'Invalid Data, this may email or password')
    except Exception as e:
        e
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logoutView(request):
    logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('accounts:login')
