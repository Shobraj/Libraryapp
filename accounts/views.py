from django.contrib.auth import (
    login, 
    logout, 
    get_user_model, 
    authenticate
    )
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm

# Create your views here.
def login_view(request):
    next = request.GET.get('next')
    title = 'Login' 
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('booklist')
    return render(request, "forms.html", {'form':form, 'title':title})

def register_view(request):
    next = request.GET.get('next')
    title = 'register' 
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('booklist')
    context = {'form': form, 'title': title}
    return render(request, "forms.html", context)

def logout_view(request):
    logout(request)
    return render(request, "forms.html", {})