from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('itinerary/<int:pk>/', views.itinerary_detail, name='itinerary_detail'),
    path('my-itineraries/', views.my_itineraries, name='my_itineraries'),
    path('all-itineraries/', views.all_itineraries, name='all_itineraries'),
]
