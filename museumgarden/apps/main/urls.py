from django.urls import path
from .views import *


app_name = 'main'
urlpatterns = [
    path('', ShowView.as_view(),name='index'),
]