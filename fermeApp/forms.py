
from django import forms
from .models import Cliente, DetalleOrden, InvProducto, OrdenCompra, Proveedor
from django.contrib.auth.forms import UserCreationForm  # Permite crear usuarios del sistema
from django.contrib.auth.models import User #Podemos usar metodos para user actual 

class FormRegistroCli(forms.ModelForm):

    contrasenia = forms.CharField(widget= forms.PasswordInput)

    class Meta:
        model = Cliente
        fields = ["nombre", "rut_cli", "p_apellido", "s_apellido", "email", "telefono", "usuario", "contrasenia", "pertenencia_emp"]

# REGISTRO DJANGO USUARIOS
class NuevoUserCreationForm(UserCreationForm):

    first_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', "email", "password1", "password2"]

#  AGREGAR
class AddProveedor(forms.ModelForm):
    
    class Meta:
        model = Proveedor
        fields = ["rut", "rubro", "celular", "domicilio"]

        
class AddOrden(forms.ModelForm):

    class Meta:
        model = OrdenCompra
        fields = '__all__'

class AddDetalleOrden(forms.ModelForm):

    class Meta:
        model = DetalleOrden
        fields = ["nombre" , "cantidad", "precio", "descuento", "observaciones", "proveedor_id_prov"]

class AddDetalle(forms.ModelForm):

    class Meta:
        model = DetalleOrden
        fields = ["nombre" , "cantidad", "precio", "descuento", "observaciones"]

class AddProducto(forms.ModelForm):
    
    class Meta:
        model = InvProducto
        fields = ['nombre', 'precio', "fecha_venc", "stock", "stock_crit", "stock_max","fam_producto_id_fam", "tipo_producto_id_tipo", 'marca', 'imagen', 'categoria']

# MODIFICAR
class ModificarProveedor(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ["nombre", "rut", "rubro", "celular", "domicilio" ]

class ModificarIdProveedor(forms.ModelForm):

    class Meta:
        model = DetalleOrden
        fields = ["proveedor_id_prov" ]

class ModificarProducto(forms.ModelForm):
    
    class Meta:
        model = InvProducto
        fields = ['nombre', 'precio', "fecha_venc", "stock", "stock_crit", "stock_max","fam_producto_id_fam", "tipo_producto_id_tipo", 'marca', 'imagen', 'categoria']

    
# CLIENTE
class AddCliente(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ["rut_cli", "s_apellido", "telefono", "pertenencia_emp", "direccion"]

class ModificarCliente(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ["usuario", "nombre", "email" ,"p_apellido", "s_apellido", "telefono", "pertenencia_emp", "direccion"]

# class ModificarDjangoCliente(UserCreationForm):

#     first_name = forms.CharField(required=True)
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', "email"]

# PRODUCTO
# class AddNroOrden(forms.ModelForm):

#     class Meta:
#         model= OrdenCompra
#         fields = ["nro_orden"]