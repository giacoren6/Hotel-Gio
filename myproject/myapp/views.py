from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def rooms(request):
    return render(request, 'rooms.html')