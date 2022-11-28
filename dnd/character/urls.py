from django.urls import path

from . import views

app_name = "character"

urlpatterns = [
    path("save", views.save, name="save"),
    path("", views.index, name="load"),
    path("load/<str:charname>", views.load, name="loadchar")
]


# path("/<str:name>",views.load, name="load")
# quiero que cuando cargue un pj lo haga en character/nombre del pj buscado
