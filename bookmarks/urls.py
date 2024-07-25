from django.urls import path
from . import views

app_name = 'bookmarks'

urlpatterns = [
    path('bookmark_list/', views.bookmark_list, name='bookmark_list'),
    path('bookmark_create/', views.bookmark_create, name='bookmark_create'),
    path('bookmark_delete/', views.bookmark_delete, name='bookmark_delete'),
    path('bookmark_edit/', views.bookmark_edit, name='bookmark_edit'),
]

