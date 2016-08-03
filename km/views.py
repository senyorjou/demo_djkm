from django.shortcuts import render
from django.http import JsonResponse

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


def province(request, province_id):
    ctx = {
        'title': 'DJ KM v.0.1 - Locations',
        'h1': 'Province',
        'province': Province.objects.get(id=province_id)
    }
    return render(request, 'km/province.html', ctx)


def locations(request):
    locs = Location.objects.all() \
                           .order_by('province__name') \
                           .order_by('name')

    ctx = {
        'title': 'DJ KM v.0.1 - Locations',
        'h1': 'List of locations',
        'locations': locs
    }

    if request.META['CONTENT_TYPE'] == 'application/javascript':
        json_data = [{'id': l.id, 'name': l.name, 'zip_code': l.zip_code}
                     for l in locs]

        return JsonResponse(json_data, safe=False)

    return render(request, 'km/locations.html', ctx)
