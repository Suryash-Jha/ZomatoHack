from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('History/', views.serviceHistory, name='home'),
    path('Requests/', views.serviceRequestList, name='home'),
    path('Offer/<str:id>', views.serviceOffer, name='home'),
    path('BuildProfile/', views.serviceProfileBuilder, name='buildProfile'),
    path('Profile/', views.serviceProfile, name='home'),
    path('login/', views.login, name='login'),
    path('signUp/', views.signUp, name='signUp'),
    
]