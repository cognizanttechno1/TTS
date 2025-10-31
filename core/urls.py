from django.urls import path
from . import views

urlpatterns = [
    path('', views.text_list, name='text_list'),
    path('text/english/<int:pk>/', views.text_english_read, name='text_english_read'),
    path('text/urdu/<int:pk>/', views.text_urdu_read, name='text_urdu_read'),
]
