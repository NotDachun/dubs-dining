from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse('<h1>hi</h1>')
    return render(request, 'dining_visualizer/firstPage.html')

def visualization(request):
    return render(request, 'dining_visualizer/visualization.html', {'title': 'Visualization'})
