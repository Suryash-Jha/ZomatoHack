from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "client/home.html")

def clientHistory(request):
    return render(request, "client/clientHistory.html")

def findService(request):
    return render(request, "client/findService.html")

def clientHistoryItem(request, id):
    return render(request, "client/clientHistoryItem.html")

def clientOffer(request):
    return render(request, "client/clientOffer.html")

def Profile(request):
    return render(request, "client/Profile.html")

def login(request):
    return render(request, "client/login.html")

def signUp(request):
    return render(request, "client/signUp.html")

def checkout(request):
    return render(request, "client/checkout.html")
    

