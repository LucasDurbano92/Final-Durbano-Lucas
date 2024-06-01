from django.urls import path
from . import views

app_name = "Calculo"

urlpatterns = [
    path('', views.lista_presupuestos, name='lista_presupuestos'),
    path('presupuestos/', views.lista_presupuestos, name='lista_presupuestos'),
    path('presupuestos/crear/', views.crear_presupuesto, name='crear_presupuesto'),
    path('presupuestos/<int:pk>/', views.ver_presupuesto, name='ver_presupuesto'),
    path('presupuestos/<int:pk>/borrar/', views.borrar_presupuesto, name='borrar_presupuesto'),
    path('borrar-todos-presupuestos/', views.borrar_todos_presupuestos, name='borrar_todos_presupuestos'),
    path('presupuestos/<int:pk>/enviar_a_venta/', views.enviar_a_venta, name='enviar_a_venta'),
    path('presupuestos/enviar_todos_a_venta/', views.enviar_todos_a_venta, name='enviar_todos_a_venta'),
    path('cliente/nuevo/', views.cliente_nuevo, name='cliente_nuevo'),
    
]
