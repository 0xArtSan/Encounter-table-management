from django.urls import path

from . import views

app_name = "character"

urlpatterns = [
    path("save", views.save, name="save"),
    path("", views.load, name="load")
]


# path("/<str:name>",views.load, name="load")
# quiero que cuando cargue un pj lo haga en character/nombre del pj buscado
