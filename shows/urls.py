from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('shows/', views.shows,name="shows"),
    path('shows/new/',views.addnew,name="new"),
    path('shows/delete/',views.deleteshow,name="delete"),
    path('shows/edit/',views.editshow,name="edit")
]