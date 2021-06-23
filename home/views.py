from django.shortcuts import render


def index(request):
    # View returnig index page from home
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')
