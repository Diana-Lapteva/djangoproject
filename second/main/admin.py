from django.contrib import admin
from .models import Person, Program, Management, CourseMate

@admin.register(CourseMate)
class CourseMateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'average_grade', 'email', 'phone')
    list_filter = ('gender',)
    ordering = ['-average_grade']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'is_head')
    list_filter = ('is_head',)
