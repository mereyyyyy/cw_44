from django.urls import path
from .views import ThreadListView  # или thread_list, если это функция

urlpatterns = [
    path("threads/", ThreadListView.as_view(), name="thread_list"),  # Для класса
    # path("threads/", thread_list, name="thread_list"),  # Для функции
]
