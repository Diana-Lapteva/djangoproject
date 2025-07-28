from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.TextField()

    def __str__(self):
        return self.full_name

class Program(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField()
    what_to_learn = models.TextField()
    advantages = models.TextField()
    prospects = models.TextField()

    def __str__(self):
        return self.name

class Management(models.Model):
    full_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='management/')
    email = models.EmailField()
    is_head = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

class CourseMate(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]

    full_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='mates/')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    average_grade = models.FloatField(default=0)


    def __str__(self):
        return self.full_name
