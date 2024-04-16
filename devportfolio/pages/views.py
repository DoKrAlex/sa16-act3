from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def work(request):
    return render(request, 'pages/work.html')

def contact(request):
    return render(request, 'pages/contact.html')
