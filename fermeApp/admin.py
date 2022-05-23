from django.contrib import admin
from .models import *

# ADMIN USUARIOS
class ProveedorAdmin (admin.ModelAdmin):
    list_display = ["id_prov", "nombre", "rut", "rubro", "habilitado", "userid"]

class VendedorAdmin (admin.ModelAdmin):
    list_display = ["rut_ven", "nombre", "p_apellido", "usuario", "habilitado"]

class EmpleadoAdmin (admin.ModelAdmin):
    list_display = ["rut_emp", "nombre", "p_apellido", "usuario", "habilitado"]

class ClienteAdmin (admin.ModelAdmin):
    list_display = ["nombre","rut_cli", "p_apellido", "usuario", "pertenencia_emp", "habilitado"]

# ADMIN PRODUCTOS
class FamProductoAdmin (admin.ModelAdmin):
    list_display = ["id_fam", "descripcion"]

class TipoProductoAdmin (admin.ModelAdmin):
    list_display = ["id_tipo", "descripcion"]


class InvProductoAdmin (admin.ModelAdmin):
    list_display = ["id_prod", "nombre", "precio", "stock", "stock_crit", "stock_max", "habilitado", "fam_producto_id_fam", "marca", "tipo_producto_id_tipo", "categoria"]

# ADMIN ORDEN COMPRA
class DetalleOrdenAdmin (admin.ModelAdmin):
    list_display = ["orden_compra_nro_orden", "nombre", "proveedor_id_prov", "cantidad", "precio", "descuento", "recibido"]

class OrdenCompraAdmin (admin.ModelAdmin):
    list_display = ["nro_orden", "fecha", "empleado_rut_emp"]

# ADMIN VENTA
class VentaDocAdmin (admin.ModelAdmin):
    list_display = ["nro_doc", "fecha", "tipo_venta", "valor_neto", "iva", "vendedor_rut_ven", "cliente_rut_cli"]

class DetalleVentaAdmin (admin.ModelAdmin):
    list_display = ["venta_doc_nro_doc", "inv_producto_id_prod", "cantidad", "precio", "descuento"]

# Register your models here.
admin.site.register(Vendedor, VendedorAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(FamProducto, FamProductoAdmin)
admin.site.register(VentaDoc, VentaDocAdmin)
admin.site.register(InvProducto, InvProductoAdmin)
admin.site.register(OrdenCompra, OrdenCompraAdmin)
admin.site.register(DetalleOrden, DetalleOrdenAdmin)
admin.site.register(DetalleVenta, DetalleVentaAdmin)
admin.site.register(TipoProducto, TipoProductoAdmin)
