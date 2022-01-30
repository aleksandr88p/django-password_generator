from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    # return HttpResponse("Hello there friends")
    return render(request, 'generator/home.html')  #, {'password': 'abra-kadabra'})

def about(request):
    return render(request, 'generator/about.html')

def dogs(request):
    return HttpResponse("<h1>Maya is so quite</h1>")

def password(request):
    password_to_generte = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = request.GET.get('length')

    if request.GET.get('uppercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    for i in range(int(length)):
        password_to_generte += random.choice(characters)

    return render(request, 'generator/password.html', {'password': password_to_generte})