from django.urls import path

from . import views

app_name = "monster"

urlpatterns = [
    path("save", views.save, name="savemon"),
    path("", views.load, name="loadmon")
]
