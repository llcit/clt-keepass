# keepass/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *

def index(request):
    try:
        entry = Entry.objects.all().order_by('id')
    except App.DoesNotExist:
        raise Http404("Keepass does not exist.")

    return render(request, 'keepass/index.html', {'entry': entry,})
