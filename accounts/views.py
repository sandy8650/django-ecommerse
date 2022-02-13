from django.shortcuts import redirect, render

from .forms import RegisterationForm


def register(request):
    if request.method == "POST":
        form = RegisterationForm(request.POST)   
        if form.is_valid():
            form.save()
            return redirect('products:home')
    else:
        form = RegisterationForm()
    context = {
        'form': form,
    }   
    return render(request, 'accounts/register.html', context)


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return 
