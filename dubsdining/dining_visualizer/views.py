from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'dining_visualizer/firstPage.html')

def visualization(request):
    return render(request, 'dining_visualizer/visualization.html')
