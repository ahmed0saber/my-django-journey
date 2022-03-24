from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("view1/", views.view1, name="view 1"),
]