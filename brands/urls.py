
from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.brands),
    path('memory/', views.memory),
]