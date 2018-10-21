from django.shortcuts import render
from django.http import HttpResponse
from . import newscraper

def home(request):
    return render(request, 'dining_visualizer/firstPage.html')

def visualization(request):
    get_data(request)
    return render(request, 'dining_visualizer/visualization.html', {'title': 'Visualization'})

def datas(request):
    return render(request, 'dining_visualizer/newTable.html', {'title': 'Data'})

def get_data(request):
    newscraper.get_data_selenium(request.POST['UWNetID'], request.POST['Password'])


