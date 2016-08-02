from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^provinces$', views.provinces, name='provinces'),
    url(r'^locations$', views.locations, name='locations'),
    url(r'^', views.index, name='index'),
]