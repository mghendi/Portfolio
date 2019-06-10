from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    home_title = "Hi !"
    context = {"title": home_title}
    #doc = "<h1>{title}</h1>".format(title=title)
    #django_rendered_doc = "<h1>{{title}}</h1>".format(title=title)
    return render(request, "home.html", context)

def work(request):
    context = {"title": "Things I've Learnt"}
    return render(request, "work.html", context)

def blog(request):
    context = {"title": "Tips, Tricks & Tutorials"}
    return render(request, "blog.html", context)

def resume(request):
    context = {"title": "Resume"}
    return render(request, "resume.html", context)