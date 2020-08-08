from django.shortcuts import render
import datetime


def home(request):
    name = 'Dave'
    date = datetime.datetime.now()
    _context = {'name': name, 'date': date}
    return render(request, 'home.html', _context)
