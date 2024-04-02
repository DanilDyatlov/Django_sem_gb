from django.urls import path
from . import views

urlpatterns = [
    path('heads_and_tails/', views.heads_and_tails, name='heads_and_tails'),
    path('heads_and_tails/stats/<n>', views.stats, name='stats'),
]