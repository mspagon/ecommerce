from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context = {
        "title": "home",
        "content": "Welcome to the home page!"
    }
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "about",
        "content": "Welcome to the about page!"
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    context = {
        "title": "contact",
        "content": "Welcome to the contact page!"
    }
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get('fullname'))
    return render(request, r"contact/view.html", context)
