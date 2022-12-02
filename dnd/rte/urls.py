from django.urls import path

from . import views

app_name = "rte"

urlpatterns = [
    path("save/", views.saverte, name="saverte"),
    path("", views.loadrte, name="loadrte")
]
