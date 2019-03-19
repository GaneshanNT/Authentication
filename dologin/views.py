from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def Loginview(request):
    count = User.objects.count()
    context = {
        'count':count
    }
    return render(request,'index.html',context)

def Signupview(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:    
        form = UserCreationForm()
        context = {
            'form':form
        }
        return render(request,'registration/signup.html',context)

@login_required
def secret(request):
    return render(request,'secretpage.html')

class Classview(LoginRequiredMixin,TemplateView):
    template_name='classview.html'


