from django.urls import path
from . import views

urlpatterns = [
    path('heads_and_tails/', views.heads_and_tails, name='heads_and_tails'),
    path('roll_the_dice/', views.roll_the_dice, name='roll_the_dice'),
    path('random_number/', views.random_number, name='random_number'),
]