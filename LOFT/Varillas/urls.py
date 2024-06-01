from django.urls import path
from . import views

app_name="Varillas"

urlpatterns = [
    path("", views.index, name="index"),
    path("lista_ventas/", views.lista_ventas, name="lista_ventas"),
]