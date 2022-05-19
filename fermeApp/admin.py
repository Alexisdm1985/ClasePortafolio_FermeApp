from django.contrib import admin
from .models import *
#  Vendedor, Empleado, Proveedor, Cliente, FamProducto, Parametro, VentaDoc, InvProducto, OrdenCompra, DetalleOrden, DetalleVenta, OfertaProd, DetalleOferta

# Register your models here.
admin.site.register(Vendedor)
admin.site.register(Empleado)
admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(FamProducto)
admin.site.register(Parametro)
admin.site.register(VentaDoc)
admin.site.register(InvProducto)
admin.site.register(OrdenCompra)
admin.site.register(DetalleOrden)
admin.site.register(DetalleVenta)
admin.site.register(OfertaProd)
admin.site.register(DetalleOferta)