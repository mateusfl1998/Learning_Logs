from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect(to='topics_list')
        else:
            login_form = AuthenticationForm() 
    else:
        login_form = AuthenticationForm()  
        return render(request, 'login.html',{'login_form':login_form})


def registry_view(request):
    if request.method != "POST":
        user_form = UserCreationForm()
    else:
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    return render(request,'registry.html', {'user_form':user_form})

def logout_view(request):
    logout(request)
    return redirect('home')