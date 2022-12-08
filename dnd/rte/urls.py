from django.urls import path

from . import views

app_name = "rte"

urlpatterns = [
    path("save/", views.table, name="table"),
    path("", views.loadrte, name="loadrte"),
    path("initiative", views.prepcomb, name="prepcomb")
]
