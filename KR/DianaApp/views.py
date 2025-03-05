from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    # http://127.0.0.1:8000/responseApp/
    return HttpResponse("По умолчанию DianaApp")

def html(request):
    # http://127.0.0.1:8000/responseApp/html/
    now = datetime.datetime.now()
    html = "<html><body>Сейчас %s.</body></html>" % now
    return HttpResponse(html)

def f_str(request, str_value):
    # http://127.0.0.1:8000/responseApp/f_str/abc
    print("str_value: ",  str_value)

    return HttpResponse(f"<p>f_str, str_value:  {str_value}</p>")


def f_int(request, int_value):
    # http://127.0.0.1:8000/responseApp/f_int/12345
    print(type(int_value), int_value)
    return HttpResponse(f"f_int, int_value: {int_value} ")


def f_slug(request, slug_value):
    # http://127.0.0.1:8000/responseApp/f_slug/building-your_1st-django-site
    print(type(slug_value), slug_value)
    return HttpResponse(f"f_slug, slug_value: {slug_value}")


def f_str_int_slug(request, str_value, int_value, slug_value):
    # http://127.0.0.1:8000/responseApp/f_str_int_slug/x=1&y=2/123/1st-django-site
    print(type(str_value), str_value)
    print(type(int_value), int_value)
    print(type(slug_value), slug_value)
    return HttpResponse(
        f"f_str,  str_value: {str_value} <br>f_int, f_int: {int_value} <br>f_slug, slug_value: {slug_value}"
    )

def f_path(request, path_value):
    path_elements = path_value.split("/")
    x = (path_elements[2].split("="))[1]
    return HttpResponse(f"x:  {x}")