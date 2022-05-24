# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from pickle import FALSE
from django.db import models

# OPCIONES
opciones_habilitado = [
    [0, "No"],
    [1, "Si"]
]
opciones_categoria = [
    ['Herramientas', 'Herramientas'],
    ['Gasfiteria', 'Gasfiteria'],
    ['Hogar', 'Hogar'],
    ['Construccion', 'Construccion']
]

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cliente(models.Model):
    rut_cli = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=50)
    p_apellido = models.CharField(max_length=50)
    s_apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    telefono = models.BigIntegerField()
    usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=250)
    pertenencia_emp = models.FloatField(choices=opciones_habilitado)
    tipo_usuario = models.CharField(max_length=30,default='CLIENTE')
    habilitado = models.FloatField(choices=opciones_habilitado, default=1)
        

    def __str__(self):
        return f"{self.nombre} {self.p_apellido}"

    class Meta:
        managed = False
        db_table = 'cliente'


class DetalleOrden(models.Model):
    orden_compra_nro_orden = models.ForeignKey('OrdenCompra', models.DO_NOTHING, db_column='orden_compra_nro_orden')
    proveedor_id_prov = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor_id_prov')
    nro_prod = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    descuento = models.IntegerField()
    observaciones = models.CharField(max_length=220, blank=True, null=True)
    recibido = models.FloatField(default=0, choices=opciones_habilitado)
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.orden_compra_nro_orden.__str__()

    class Meta:
        managed = False
        db_table = 'detalle_orden'
        unique_together = (('orden_compra_nro_orden', 'proveedor_id_prov', 'nro_prod'),)


class DetalleVenta(models.Model):
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    descuento = models.IntegerField()
    venta_doc_nro_doc = models.OneToOneField('VentaDoc', models.DO_NOTHING, db_column='venta_doc_nro_doc', primary_key=True)
    inv_producto_id_prod = models.ForeignKey('InvProducto', models.DO_NOTHING, db_column='inv_producto_id_prod')

    def __str__(self):
        return f"Detalle de {self.venta_doc_nro_doc}"

    class Meta:
        managed = False
        db_table = 'detalle_venta'
        unique_together = (('venta_doc_nro_doc', 'inv_producto_id_prod'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    rut_emp = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=50)
    p_apellido = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=250)
    cargo = models.CharField(max_length=50)
    tipo_usuario = models.CharField(max_length=30, default='EMPLEADO')
    habilitado = models.FloatField(choices=opciones_habilitado)


    def __str__(self):
        return f"{self.nombre} {self.p_apellido}"

    class Meta:
        managed = False
        db_table = 'empleado'


class FamProducto(models.Model):
    id_fam = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        db_table = 'fam_producto'


class InvProducto(models.Model):
    id_prod = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=250)
    precio = models.IntegerField()
    stock = models.IntegerField()
    stock_crit = models.IntegerField()
    stock_max = models.IntegerField()
    fecha_venc = models.DateField(blank=True, null=True)
    habilitado = models.FloatField(choices=opciones_habilitado, default=1)
    fam_producto_id_fam = models.ForeignKey(FamProducto, models.DO_NOTHING, db_column='fam_producto_id_fam')
    marca = models.CharField(max_length=250)
    tipo_producto_id_tipo = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='tipo_producto_id_tipo')
    imagen = models.ImageField(upload_to="productos", blank=True, null=True)
    categoria= models.CharField(choices=opciones_categoria, max_length=250)
    
    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        managed = False
        db_table = 'inv_producto'


class OrdenCompra(models.Model):
    nro_orden = models.AutoField(primary_key=True)
    fecha = models.DateField()
    empleado_rut_emp = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_rut_emp')
    
    def __str__(self):
        return self.nro_orden.__str__()

    class Meta:
        managed = False
        db_table = 'orden_compra'


class Proveedor(models.Model):
    id_prov = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    rut = models.CharField(max_length=30)
    rubro = models.CharField(max_length=50)
    celular = models.BigIntegerField()
    domicilio = models.CharField(max_length=220)
    tipo_usuario = models.CharField(max_length=30, default='PROVEEDOR')
    habilitado = models.FloatField(choices=opciones_habilitado, default=1)
    userid = models.IntegerField()

    def __int__(self):
        return self.id_prov

    def __str__(self):
        return f"{self.id_prov}-{self.nombre} "

    class Meta:
        managed = False
        db_table = 'proveedor'


class TipoProducto(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.descripcion}"

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class Vendedor(models.Model):
    rut_ven = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=50)
    p_apellido = models.CharField(max_length=50)
    s_apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    telefono = models.BigIntegerField()
    usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=250)
    tipo_usuario = models.CharField(max_length=30, default='VENDEDOR')
    habilitado = models.FloatField(choices=opciones_habilitado)

    def __str__(self):
        return f"{self.nombre} {self.p_apellido}"

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

    def __str__(self):
        return f"Venta nro {self.nro_doc}"

    class Meta:
        managed = False
        db_table = 'venta_doc'
