from django.urls import path
from .views import * 

app_name = 'search'
urlpatterns = [
    path('', SeachResultsView.as_view(), name='search_results'),
]
 