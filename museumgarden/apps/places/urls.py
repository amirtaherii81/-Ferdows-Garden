from django.urls import path
from .views import *

app_name = 'places'
urlpatterns=[
    path('history/', ShowGardenHistoryView.as_view(), name='history'),
    path('parts/', ShowGardenPartsView.as_view(), name='parts'),
    path('part/<int:id>', ShowPartDetailView.as_view(), name='part_detial'),
    path('pdf_path/', DownloadPathGardenView.as_view(), name='pdf_path'),
    path('ticket_price/', ShowTimeRuleView.as_view(), name='ticket_price'),
    path('contact/', ContactView.as_view(), name='contact'),
]