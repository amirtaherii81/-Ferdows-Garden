from django.urls import path
from .views import *

app_name = 'workshops'
urlpatterns = [
    path('', ShowWorkshopView.as_view(), name='show'),
    path('workshopreport/<int:pk>', ShowWorkshopReport.as_view(), name='workshopreport')
]
