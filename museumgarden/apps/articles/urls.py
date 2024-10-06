from django.urls import path
from .views import *

app_name = 'articles'
urlpatterns = [
    path('', ShowArticlesView.as_view(), name='blog'),
    path('<str:slug>/', ShowBlogDetailsView.as_view(), name='blog_details'),
    path('articlepdf/<int:article_id>', ShowArticlePdfView.as_view(), name='article_pdf'),
]
