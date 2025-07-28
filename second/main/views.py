from django.shortcuts import render
from .models import Person, Program, Management, CourseMate

def index(request):
    person = Person.objects.first()
    return render(request, 'index.html', {'person': person})

def program(request):
    program = Program.objects.first()
    return render(request, 'program.html', {'program': program})

def management(request):
    management = Management.objects.all()
    return render(request, 'management.html', {'management': management})

def mates(request):
    mates = CourseMate.objects.all()

    # Фильтрация по полу
    gender = request.GET.get('gender')
    if gender in ['M', 'F']:
        mates = mates.filter(gender=gender)

    # Сортировка по среднему баллу
    sort = request.GET.get('sort')
    if sort == 'asc':
        mates = mates.order_by('average_grade')
    elif sort == 'desc':
        mates = mates.order_by('-average_grade')

    return render(request, 'mates.html', {'mates': mates})
