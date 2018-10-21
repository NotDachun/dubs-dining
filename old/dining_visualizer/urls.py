from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='visualizer-home'),
    path('visualization/', views.visualization, name='visualization'),
    path('data/', views.datas, name='hidden-data')
]
