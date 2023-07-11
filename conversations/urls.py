from django.urls import path
from .views import create_conversation, inbox, detail

app_name = 'conversation'

urlpatterns = [
    path('<int:item_pk>/', create_conversation, name='new'),
    path('detail/<int:conversation_pk>/', detail, name='detail'),
    path('inbox/', inbox, name='inbox'),
]
