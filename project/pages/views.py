from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# *args and **kwargs capture requests here.


def homepage_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World!</h1>")
    context = {
        "name": "Utkarsh",
        "number": 132456,
        "my_list": [13, 35, 654]
    }
    return render(request, "home.html", context)
