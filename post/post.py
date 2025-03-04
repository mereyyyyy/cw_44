from django.urls import path
from .views import thread_list, thread_detail, thread_create, post_create

urlpatterns = [
    path('threads/', thread_list, name='thread_list'),
    path('threads/<int:id>/', thread_detail, name='thread_detail'),
    path('threads/create/', thread_create, name='thread_create'),
    path('posts/create/', post_create, name='post_create'),
]
