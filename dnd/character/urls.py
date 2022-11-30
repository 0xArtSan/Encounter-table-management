from django.urls import path

from . import views

app_name = "character"

urlpatterns = [
    path("save", views.save, name="save"),
    path("", views.load, name="load")
]
