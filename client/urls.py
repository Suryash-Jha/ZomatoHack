from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('History/<str:cliendId>/', views.clientHistory, name='clientHistory'),
    path('Find/', views.findService, name='findService'),
    path('History/<int:id>/', views.clientHistoryItem, name='clientHistoryItem'),
    path('Offers/', views.clientOffer, name='clientOffer'),
    path('Profile/<str:id>', views.Profile, name='Profile'),
    path('login/', views.login, name='login'),
    path('signUp/', views.signUp, name='signUp'),
    path('checkout/', views.checkout, name='checkout'),

]