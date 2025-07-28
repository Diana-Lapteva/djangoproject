from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('program/', views.program, name='program'),
    path('management/', views.management, name='management'),
    path('mates/', views.mates, name='mates'),
]
