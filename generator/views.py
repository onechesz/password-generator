from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('special'):
        characters.extend('!@#$%^&*()_+"№;:?')

    if request.GET.get('numbers'):
        characters.extend('01234567890')

    length = int(request.GET.get('length', 12))
    generated_password = ''

    for i in range(length):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': generated_password})


def about(request):
    return render(request, 'generator/about.html')
