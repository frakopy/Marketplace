from django.urls import path
from .views import detail, new_item, delete, edit, search

urlpatterns = [
    path('search', search, name='search'),
    path('<int:pk>/', detail, name='item_detail'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('new/', new_item, name='new_item'),
]
