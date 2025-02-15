from django.shortcuts import render

def home(requests):
    return render('home.html')

def custom_excuse(requests):
    return render('custom_excuse.html')