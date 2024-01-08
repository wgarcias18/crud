from django.urls import path
from .views import listar_producto, crear_producto, eliminar_producto, editar_producto

urlpatterns = [
    path('', listar_producto, name='producto'),
    path('nueva/', crear_producto, name='nuevo_producto'),
    path('eliminar_producto/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('editar_producto/<int:producto_id>/', editar_producto, name='editar_producto'),

]