from django.urls import path
from .views import eliminar_proveedor, modificarProveedor, emp_orden, addProveedor, emp_productos, eliminar_producto, index, registro, contacto, productos, nosotros, empleado, addProducto, modificarProducto, emp_proveedor, addOrden

urlpatterns = [
    # Global
    path('', index, name='index'),
    path('registro/', registro, name='registro'),
    path('contacto/', contacto, name='contacto'),
    path('productos/', productos, name='productos'),
    path('nosotros/', nosotros, name='nosotros'),
    # Empleado
    path('homeEmp/', empleado, name='homeEmp'),
    path('emp_productos/', emp_productos, name='emp_productos'),
    path('emp_proveedor/', emp_proveedor, name='emp_proveedor'),
    path('emp_orden/', emp_orden, name='emp_orden'),
    path('addOrden/', addOrden, name='addOrden'),
    path('addProducto/', addProducto, name='addProducto'),
    path('addProveedor/', addProveedor, name='addProveedor'),
    path('modificarProducto/<id>/', modificarProducto, name='modificarProducto'),
    path('modificarProveedor/<id_prov>/', modificarProveedor, name='modificarProveedor'),
    path('eliminar_producto/<id>/', eliminar_producto, name='eliminar_producto'),
    path('eliminar_proveedor/<id_prov>/', eliminar_proveedor, name='eliminar_proveedor'),
    

    # Cliente
    # Vendedor

    # Proveedor
]
