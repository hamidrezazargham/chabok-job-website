from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from .forms import CreateUserForm
from .serializers import jobSeekerHomePageSerializer
from .usecases import *


def sign_up(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Acount was created successfuly")
            return redirect('login')
    context = {'form': form}
    return render(request, 'signup.html', context)


def login_user(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')


def home_page(request):
    context = {}
    if request.method == "GET":
        user = request.user
        if user.get_role() == "EMPLOYER":
            context = employerHomePageSerializer(user).data
        else:
            context = jobSeekerHomePageSerializer(user).data
    return render(request, 'main.html', context)


def view_job(request, pk):
    context = {}
    if request.method == "GET":
        user = request.user
        job_offer = get_jobOffer_by_id(pk)
        if user.get_role() == "EMPLOYER":
            context = viewJobApplicantsSerializer(job_offer).data
            return render(request, 'viewjobapplicants.html', context)
        else:
            context = viewJobsSerializer(job_offer).data
            return render(request, 'viewjobs.html')
    return render(request, 'login.html', context)
    
