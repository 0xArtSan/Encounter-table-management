from django.urls import path

from . import views

app_name = "encounter"

urlpatterns = [
    path("", views.combat, name="combat")
]
