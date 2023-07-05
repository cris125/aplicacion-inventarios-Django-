from django.urls import path
from . import views

urlpatterns = [
    path('',views.add,name='add'),
    path('AgregarProducto',views.agre,name='AgregarProducto'),
    path('eliminarP/<id>', views.eliminar),
    path('edicionP/<id>', views.edicionP),
    path('editarP/<id>', views.editarP),
]
