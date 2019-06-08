from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, "home.html")

def work(request):
    return render(request, "work.html")

def blog(request):
    return render(request, "blog.html")

def resume(request):
    return render(request, "resume.html")