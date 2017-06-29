from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^([0-9]+)/$', views.details, name='details'),
]