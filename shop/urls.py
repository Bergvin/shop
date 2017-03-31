from django.conf.urls import url
from .models import Cards

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.cart, name='cart'),
    url(r'^$', views.checkout, name='checkout'),
] 