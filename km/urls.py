from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^provinces$', views.provinces, name='provinces'),
    url(r'^provinces/(?P<province_id>[0-9]+)$', views.province, name='province'),
    url(r'^locations$', views.locations, name='locations'),
    url(r'^customers$', views.CustomerList.as_view(), name='customers'),
    url(r'^products$', views.ProductList.as_view(), name='products'),
    url(r'^products/(?P<pk>[0-9]+)$', views.ProductView.as_view(),
        name='product'),
    url(r'^', views.index, name='index'),
]