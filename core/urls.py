from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:room_name>/', views.room, name='room'),
]
