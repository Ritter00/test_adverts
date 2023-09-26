from django.urls import path, include
from rest_framework import routers
from .views import *

app_name = 'adverts'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/advert-list/', snippet_list, name='snippet_list'),
    path('api/advert/<int:pk>/', snippet_detail, name='snippet_detail'),
]