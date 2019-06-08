from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<h1>Home</h1>")

def work(request):
    return HttpResponse("<h1>Portfolio</h1>")

def blog(request):
    return HttpResponse("<h1>Things I'm Learning</h1>")

def resume(request):
    return HttpResponse("<h1>Resume</h1>")