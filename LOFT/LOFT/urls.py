from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),
    path("Varillas/", include("Varillas.urls")),
    path("Calculo/", include("Calculo.urls"))
]
