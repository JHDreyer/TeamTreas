from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate

from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView,FormView)

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ContactForm

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self,form):
        form.send_email()
        return super().form_valid(form)
