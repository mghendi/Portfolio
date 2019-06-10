from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    home_title = "Hi, I'm Sammy."
    #doc = "<h1>{title}</h1>".format(title=title)
    #django_rendered_doc = "<h1>{{title}}</h1>".format(title=title)
    return render(request, "home.html", {"title": home_title})

def work(request):
    return render(request, "work.html", {"title": "Things I've Learnt"})

def blog(request):
    return render(request, "blog.html", {"title": "Tips, Tricks & Tutorials"})

def resume(request):
    return render(request, "resume.html", {"title": "Resume"})