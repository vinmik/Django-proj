from django.shortcuts import render
from django.http import HttpResponse
import random

def some(request):
    return render(request,'generator/some.html')

def about(request):
    return render(request,'generator/about.html')

def password(request):

    result= ''
    char=list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.GET.get('length',8))

    if request.GET.get('numbers'):
        char.extend(list('0123456789'))

    if request.GET.get('upper'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        char.extend(list('/*-+@!#$%^&*()~'))

    
    for i in range(length):
        result=result+random.choice(char)

    return render(request,'generator/password.html', {'password':result})

