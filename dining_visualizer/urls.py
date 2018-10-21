from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='visualizer-home'),
    path('visualization', views.visualization, name='visualization'),
]
