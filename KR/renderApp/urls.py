from django.urls import path
from . import views

app_name = "renderApp"
urlpatterns = [
    path("", views.index, name="index"),
    path("greet/<str:path_value>", views.greet, name="greet"),
    path("search_price/", views.search_price, name="search_price"),
    path("money_exchange/", views.money_exchange, name="money_exchange"),
    path("pages/<path:path_value>", views.pages, name="pages"),
    path("objects_arrays/", views.objects_arrays, name="objects_arrays"),
    path("programm_info/", views.programm_info, name='programm_info'),
]
