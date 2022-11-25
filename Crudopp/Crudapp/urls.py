from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.add_show, name='home' ),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('<int:id>/', views.update_data, name='updatedata'),
]