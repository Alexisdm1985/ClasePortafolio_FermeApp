from django.urls import path
from .views import homeProveedor, reportes, producto, eliminar_cliente, modificarCliente, emp_cliente, addCliente , comprasCliente, administrarCliente, homeUsuarios, addDetalle ,modificarDetalle, detalleOrden, modificarOrden, eliminar_proveedor, modificarProveedor, emp_orden, addProveedor, emp_productos, eliminar_producto, index, registro, contacto, productos, nosotros, empleado, addProducto, modificarProducto, emp_proveedor, addOrden

urlpatterns = [
# Global
    path('', index, name='index'),
    path('registro/', registro, name='registro'),
    path('contacto/', contacto, name='contacto'),
    path('productos/', productos, name='productos'),
    path('producto/<id_prod>', producto, name='producto'),
    path('nosotros/', nosotros, name='nosotros'),
# EMPLEADO
    path('homeEmp/', empleado, name='homeEmp'),
    path('reportes/', reportes, name='reportes'),
# Productos
    path('emp_productos/', emp_productos, name='emp_productos'),
    path('addProducto/', addProducto, name='addProducto'),
    path('modificarProducto/<id>/', modificarProducto, name='modificarProducto'),
    path('eliminar_producto/<id>/', eliminar_producto, name='eliminar_producto'),
# Ordenes
    path('emp_orden/', emp_orden, name='emp_orden'),
    path('addOrden/', addOrden, name='addOrden'),
    path('addDetalleOrden/<nro_orden>', addDetalle, name='addDetalle'),
    path('modificarOrden/<nro_orden>/', modificarOrden, name='modificarOrden'),
    path('emp_detallesOrden/<nro_orden>/', detalleOrden, name='detalleOrden'),
    path('modificarDetalleOrden/<nro_orden>/<nro_prod>/', modificarDetalle, name='modificarDetalle'),
# Proveedores
    path('emp_proveedor/', emp_proveedor, name='emp_proveedor'),
    path('addProveedor/', addProveedor, name='addProveedor'),
    path('modificarProveedor/<id_prov>/', modificarProveedor, name='modificarProveedor'),
    path('eliminar_proveedor/<id_prov>/', eliminar_proveedor, name='eliminar_proveedor'),        
    path('homeProveedor/', homeProveedor, name='homeProveedor'),        

# Clientes
    path('homeUsuarios/', homeUsuarios, name='homeUsuarios'),
    path('administrarCliente/', administrarCliente, name='administrarCliente'),
    path('comprasCliente/', comprasCliente, name='comprasCliente'),
    path('emp_cliente/', emp_cliente, name='emp_cliente'),
    path('addCliente/', addCliente, name='addCliente'),
    path('modificarCliente/<user_name>/', modificarCliente, name='modificarCliente'),
    path('eliminar_cliente/<rut>/', eliminar_cliente, name='eliminar_cliente'),
]
