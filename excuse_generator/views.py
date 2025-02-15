from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def custom_excuse(request):
    return render(request, 'custom_excuse.html')