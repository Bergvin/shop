from django.conf.urls import url
from .models import Cards

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]