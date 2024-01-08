from django.urls import path
from .views import listar_Proveedor,crear_Proveedor ,listar_Pais, crear_pais

urlpatterns = [
    path('', listar_Proveedor, name='proveedor'),
    path('nueva/', crear_Proveedor, name='crear_Proveedor'),
    path('listar/', listar_Pais, name='listar_Pais'),
    path('nueva/pais', crear_pais, name='crear_pais'),
    #path('eliminar_tareas/<int:tareas_id>/', eliminar_tareas, name='eliminar_tareas'),
    #path('editar_tareas/<int:tareas_id>/', editar_tareas, name='editar_tareas'),

]