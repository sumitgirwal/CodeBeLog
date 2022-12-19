from django.shortcuts import render
from .models import Post


def index(request):
    context = {}
    return render(request, 'index.html', context)
