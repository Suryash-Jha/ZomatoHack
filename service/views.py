from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "service/home.html")

@login_required(login_url='/service/login')
def serviceHistory(request):
    return render(request, "service/serviceHistory.html")

def serviceRequestList(request):
    return render(request, "service/serviceRequestList.html")

def serviceOffer(request):
    return render(request, "service/serviceOffer.html")

def serviceProfileBuilder(request):
    return render(request, "service/serviceProfileBuilder.html")

def serviceProfile(request):
    return render(request, "service/serviceProfile.html")

def login(request):
    return render(request, "service/login.html")

def signUp(request):
    return render(request, "service/signUp.html")




