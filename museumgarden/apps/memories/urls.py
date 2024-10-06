from django.urls import path
from .views import ShowMemoriesView, add_memory, like

app_name = 'memories'
urlpatterns = [
    path('show_memories/', ShowMemoriesView.as_view(), name='show_memories'),
    path('registermemory/', add_memory, name='register_memory'),
    path('like/', like, name='like'),
]
