from django.shortcuts import render

def index(request):
    ctx = {
        'title': 'DJ KM v.0.1',
        'h1': 'This is the menu page',
        'content': 'This is the menu page content',
    }

    return render(request, 'km/index.html', ctx)
