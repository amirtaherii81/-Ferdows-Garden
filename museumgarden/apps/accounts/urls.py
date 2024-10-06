from django.urls import path
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(),name='login'),
    path('logout/', LogoutUserView.as_view(),name='logout'),
]
