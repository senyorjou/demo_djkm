from django.shortcuts import render

from km.models import Location, Province


def index(request):
    ctx = {
        'title': 'DJ KM v.0.1',
        'h1': 'This is the menu page',
        'content': 'This is the menu page content',
        'locations': Location.objects.count(),
        'provinces': Province.objects.count()

    }

    return render(request, 'km/index.html', ctx)


def provinces(request):
    ctx = {
        'title': 'DJ KM v.0.1 - Locations',
        'h1': 'List of Provinces',
        'provinces': Province.objects.all().order_by('name')
    }
    return render(request, 'km/provinces.html', ctx)

def locations(request):
    ctx = {
        'title': 'DJ KM v.0.1 - Locations',
        'h1': 'List of locations',
        'locations': Location.objects.all()\
                                     .order_by('province__name')\
                                     .order_by('name')

    }
    return render(request, 'km/locations.html', ctx)