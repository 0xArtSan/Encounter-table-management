from django.urls import path

from . import views

app_name = "encounter"

urlpatterns = [
    path("", views.combat, name="loadenc"),
    path("save", views.save, name="savenc"),
    path("index", views.index, name="indexenc")
]
