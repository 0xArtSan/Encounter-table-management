from django.urls import path

from . import views

urlpatterns = [
    path("", views.save, name="save"),
    path("/<str:name>",views.load, name="load" )
]
