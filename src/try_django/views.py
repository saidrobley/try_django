# model veiw template
from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    my_title = "Home"
    context = {"title": my_title, "my_list": [1, 2, 3, 4]}
    return render(request, "home.html", context)


def about_page(request):
    return render(request, "about.html", {"title": "About us"})


def contact_page(request):
    return render(request, "contact.html", {"title": "Contact us"})
