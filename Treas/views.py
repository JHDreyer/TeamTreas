from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from .forms import RegisterForm
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')

def register(request):

    if request.method == 'POST':
        user_form = RegisterForm(request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

        else:
            print(user_form.errors)
        return reverse('register')
    else:
        user_form = RegisterForm()
    return render(request,'user-signup/register.html',{"form":user_form})


def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('account not active')
        else:
            return HttpResponse('invalid login details supplied')

    else:
        return render(request,'user-signup/login.html',{})



