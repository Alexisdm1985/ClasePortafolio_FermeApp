# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# Opciones cliente pertenece a empresa
pertenece_emp = [
    [0, "No"],
    [1, "Si"],
]

class Cliente(models.Model):
    rut_cli = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=50)
    p_apellido = models.CharField(max_length=50)
    s_apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    telefono = models.BigIntegerField()
    usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=250)
    pertenencia_emp = models.FloatField(choices=pertenece_emp)
    tipo_usuario = models.CharField(max_length=30, default='CLIENTE')
    habilitado = models.FloatField(default=1)

    class Meta:
        managed = False
        db_table = 'cliente'


class DetalleOferta(models.Model):
    proveedor_id_prov = models.OneToOneField('Proveedor', models.DO_NOTHING, db_column='proveedor_id_prov', primary_key=True)
    oferta_prod_id_prod = models.ForeignKey('OfertaProd', models.DO_NOTHING, db_column='oferta_prod_id_prod')
    precio = models.IntegerField()
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_oferta'
        unique_together = (('proveedor_id_prov', 'oferta_prod_id_prod'),)


class DetalleOrden(models.Model):
    orden_compra_nro_orden = models.OneToOneField('OrdenCompra', models.DO_NOTHING, db_column='orden_compra_nro_orden', primary_key=True)
    proveedor_id_prov = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor_id_prov')
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    descuento = models.IntegerField()
    observaciones = models.CharField(max_length=220, blank=True, null=True)
    recibido = models.FloatField()
    oferta_prod_id_prod = models.ForeignKey('OfertaProd', models.DO_NOTHING, db_column='oferta_prod_id_prod')

    class Meta:
        managed = False
        db_table = 'detalle_orden'
        unique_together = (('orden_compra_nro_orden', 'proveedor_id_prov'),)


class DetalleVenta(models.Model):
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    descuento = models.IntegerField()
    venta_doc_nro_doc = models.OneToOneField('VentaDoc', models.DO_NOTHING, db_column='venta_doc_nro_doc', primary_key=True)
    inv_producto_id_prod = models.ForeignKey('InvProducto', models.DO_NOTHING, db_column='inv_producto_id_prod')

    class Meta:
        managed = False
        db_table = 'detalle_venta'
        unique_together = (('venta_doc_nro_doc', 'inv_producto_id_prod'),)


class Empleado(models.Model):
    rut_emp = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=50)
    p_apellido = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=250)
    cargo = models.CharField(max_length=50)
    tipo_usuario = models.CharField(max_length=30)
    habilitado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'empleado'

    def __str__(self):
        return str(self.rut_emp)

class FamProducto(models.Model):
    id_fam = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=250)
    marca = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'fam_producto'


class InvProducto(models.Model):
    id_prod = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    precio = models.IntegerField()
    stock = models.IntegerField()
    stock_crit = models.IntegerField()
    stock_max = models.IntegerField()
    fecha_venc = models.DateField(blank=True, null=True)
    habilitado = models.FloatField(default=1)
    fam_producto_id_fam = models.ForeignKey(FamProducto, models.DO_NOTHING, db_column='fam_producto_id_fam')

    class Meta:
        managed = False
        db_table = 'inv_producto'


class OfertaProd(models.Model):
    id_prod = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'oferta_prod'


class OrdenCompra(models.Model):
    nro_orden = models.AutoField(primary_key=True)
    fecha = models.DateField()
    empleado_rut_emp = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_rut_emp')

    class Meta:
        managed = False
        db_table = 'orden_compra'


class Parametro(models.Model):
    id_parametro = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    valor = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'parametro'


class Proveedor(models.Model):
    id_prov = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    rut = models.CharField(max_length=30)
    rubro = models.CharField(max_length=50)
    celular = models.BigIntegerField()
    domicilio = models.CharField(max_length=220)
    tipo_usuario = models.CharField(default='PROVEEDOR', max_length=30)
    habilitado = models.FloatField(default=1)

    class Meta:
        managed = False
        db_table = 'proveedor'

    def __str__(self):
        return self.nombre


class Vendedor(models.Model):
    rut_ven = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=50)
    p_apellido = models.CharField(max_length=50)
    s_apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    telefono = models.BigIntegerField()
    usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=250)
    tipo_usuario = models.CharField(max_length=30)
    habilitado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'vendedor'


class VentaDoc(models.Model):
    nro_doc = models.AutoField(primary_key=True)
    fecha = models.DateField()
    tipo_venta = models.CharField(max_length=30)
    valor_neto = models.IntegerField()
    iva = models.IntegerField()
    vendedor_rut_ven = models.ForeignKey(Vendedor, models.DO_NOTHING, db_column='vendedor_rut_ven')
    cliente_rut_cli = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_rut_cli')

    class Meta:
        managed = False
        db_table = 'venta_doc'
