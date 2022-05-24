# Falta:
 ## MODIFICAR BASE DE DATOS || LOGICAL || RELATIONAL
 ### IMAGEN	VARCHAR2(30 BYTE)	Yes		12	
 ### Agregar campo de id donde se guardara el id del usuario Django
    - Proveedor =userid
    - Cliente
    - Vendedor
    - Empleado
#######################################
CHECK * Id prod no debe estar en el formulario de agregar producto
CHECK * Agregar nro de orden (de ahi mismo sacamos id provveedor y creamos id_producto en base de datos/django)
CHECK * Agregar detalle a orden compra
CHECK * Aplicar funcionalidad de cambio id proveedor en orden de compra (y que automaticamente se cambie en todos los detalles)
CHECK *- Agregar seccion categoria a producto
CHECK * Agregar que se pueda modificar el nombre del proveedor tanto en nuestra db como django user 

CHECK *-- Agregar modales mensaje satisfactorio
-- Agregar modales mensaje NO satisfactorio
-- Agregar modales de confirmacion de usuario

## URGENTE
CHECK * Funcionalidad agregar producto individualmente
- Funcionalidad agregar filtros en producto, orden, detalle orden, usuarios en general
- Funcionalidad agregar busqueda: Orden compra, proveedor
- Validaciones inputs formularios (todos)
- Validacion producto
- Validacion proveedor
- Validacion ordencompra
- Validacion detalleOrden

- Paginacion 
-- Crear paginas
---- producto_individual
---- prodcuto_noencontnrado
- USUARIO:
---- menuCliente
------ Administrar cuenta
-------- ?
------ Mis compras
-------- ?
- VENDEDOR:
-- Crear paginas
---- menu_vendedor
------ Administrar cuenta
-------- ?
------ Ventas
------ Buscador boleta
-------- MenuVendedorBoleta
------ Buscador factura
-------- MenuVendedorFactura

##
- EMP ADMINISTRADOR:
-- Crear paginas
---- MenuEmpleadoAdminReportes
---- MenuProveedorReportes2
- PROOVEDOR:
-- Crear paginas
---- MenuProveedor
---- MenuProveedorOrden

## FINALMENTE
- Crear readme con instrucciones de instalacion proyecto
- Arreglo/checkeo disenio todas las paginas con mockup

## Admin de la pagina todo poderoso Dios ???
- Crear paginas
-- MenuAdmin
-- MenuAdminCuenta
-- MenuAdminCuentaS
-- MenuAdminCuentaSModificar

    