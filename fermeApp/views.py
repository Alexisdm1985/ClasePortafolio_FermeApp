from .models import AuthUser, DetalleOrden, InvProducto, OrdenCompra, Proveedor, FamProducto
from .forms import AddDetalleOrden, AddOrden, NuevoUserCreationForm, AddProducto, AddProveedor, ModificarProveedor, AddDetalle
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required, login_required

# Create your views here.

# GLOBAL
def index(request):
    
    # Obtiene todos los productos
    listadoProducto = InvProducto.objects.all()
    familiaProducto = FamProducto.objects.all()
    data = {
        'productos': listadoProducto,
        'familia': familiaProducto
    }
    return render(request, 'fermeApp/index.html', data)
    
def registro(request):
    data = {
        'form': NuevoUserCreationForm()
    }
    
    # # Guarda formulario
    if request.method == 'POST':
        formulario = NuevoUserCreationForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()

            # Autentifica y loguea al usuario recien registrado
            user = authenticate(username= formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])

            login(request, user)
            return redirect(to='index')
            
            # username = formulario.cleaned_data['usuario']
            # password = formulario.cleaned_data['contrasenia']
        else:
            data["form"] = formulario

    return render(request, 'registration/registro.html', data)

def nosotros(request):
    return render(request, 'fermeApp/nosotros.html')

def productos(request):
        # Obtiene todos los productos
    producto = InvProducto.objects.all()
    data = {
        'productos': producto
    }

    if request.POST.get('nombre'):
                tituloAfiltrar = request.POST.get('nombre')
                producto = producto.filter(nombre__icontains=tituloAfiltrar)

    return render(request, 'fermeApp/productos.html', {'productos': producto})

def contacto(request):
    return render(request, 'fermeApp/contacto.html')
    
# Empleado
def empleado(request):

    userName = request.user.get_short_name()

    data = {
        'uName': userName if userName else 'Admin'
    }
    return render(request, 'fermeApp/empleado/home.html', data)

# PRODUCTOS
def emp_productos(request):

    producto = InvProducto.objects.all()
    data = {
        'productos': producto
    }

    if request.POST.get('nombre'):
                tituloAfiltrar = request.POST.get('nombre')
                producto = producto.filter(nombre__icontains=tituloAfiltrar)

    return render(request, 'fermeApp/empleado/emp_productos.html', {'productos': producto})
# @permission_required('fermeApp.add_invproducto')
def addProducto(request):
    
    data = {
        'form': AddProducto()
    }

    if request.method == 'POST':
        formulario = AddProducto(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            
            return redirect(to='emp_productos')
        else:
            data["form"] = formulario

    return render(request, 'fermeApp/empleado/addProducto.html', data)

def modificarProducto(request, id):

    producto = get_object_or_404(InvProducto, id_prod=id)

    data = {
        'form': AddProducto(instance = producto)
    }

    if request.method == 'POST':
        # En data no viene el id pero si esta en la instancia de producto
            #  porque lo buscamos con el id
        formulario = AddProducto(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to= "emp_productos")

        data['form'] = formulario

    return render(request, 'fermeApp/empleado/modificarProducto.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(InvProducto, id_prod=id)
    producto.delete()
    return redirect(to= "emp_productos")

# ORDEN COMPRA
def emp_orden(request):
    orden = OrdenCompra.objects.all()
    data = {
        'ordenes': orden
    }
    return render(request, 'fermeApp/empleado/emp_orden.html', data)

def addOrden(request):
    data = {
        'form': AddOrden(),
        'form_detalle': AddDetalleOrden()
    }

    if request.method == 'POST':
        formulario = AddOrden(data=request.POST)
        formulario_detalle = AddDetalleOrden(data=request.POST)

        if formulario.is_valid() and formulario_detalle.is_valid():
            formulario.save()
            nombre = formulario_detalle.cleaned_data['nombre']
            cantidad = formulario_detalle.cleaned_data['cantidad']
            precio = formulario_detalle.cleaned_data['precio']
            descuento = formulario_detalle.cleaned_data['descuento']
            observaciones= formulario_detalle.cleaned_data['observaciones']
            id_prov = formulario_detalle.cleaned_data['proveedor_id_prov']

            new_orden = OrdenCompra.objects.all().order_by('-nro_orden')
        
            orden = new_orden[0].nro_orden #Obtiene la ultima orden de compra ingresada
            ordenInstance = OrdenCompra.objects.get(nro_orden = orden)
            
            detalle_orden = DetalleOrden(orden_compra_nro_orden= ordenInstance, proveedor_id_prov = id_prov, cantidad = cantidad, precio = precio, descuento= descuento, observaciones = observaciones, nombre = nombre)
            detalle_orden.save()
            return redirect(to='emp_orden')
            
        else:
            data["form"] = formulario

    return render(request, 'fermeApp/empleado/addOrden.html', data)

def modificarOrden(request, nro_orden):

    ordenCompra = get_object_or_404(OrdenCompra, nro_orden=nro_orden)

    data = {
        'form': AddOrden(instance = ordenCompra)
    }

    if request.method == 'POST':
        formulario = AddOrden(data=request.POST, instance=ordenCompra)
        if formulario.is_valid():
            formulario.save()
            return redirect(to= "emp_orden")

    return render(request, 'fermeApp/empleado/modificarOrden.html', data)

def detalleOrden(request, nro_orden): # listar detalle orden 

    ordenes = DetalleOrden.objects.filter(orden_compra_nro_orden=nro_orden) #Obtiene todos los detalles de orden relacionados
    data = {
        'ordenes': ordenes
    }
    return render(request, 'fermeApp/empleado/emp_detallesOrden.html', data)

def modificarDetalle(request, nro_orden, nro_prod): # Modifita detalle orden especificado

    detalle = get_object_or_404(DetalleOrden, orden_compra_nro_orden=nro_orden, nro_prod=nro_prod)
    data = {
        'form': AddDetalle(instance=detalle)
    }

    if request.method == 'POST':
        formulario = AddDetalle(data=request.POST, instance=detalle)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='detalleOrden', nro_orden=34)

        data['form'] = formulario

    return render(request, 'fermeApp/empleado/modificarDetalleOrden.html', data)

# Proveedor
def emp_proveedor(request):
    
    proveedor = Proveedor.objects.filter(habilitado=1) #Filtra todos los proveedores con habilidado=1
    data = {
        'proveedores': proveedor
    }

    return render(request, 'fermeApp/empleado/emp_proveedor.html', data)

def addProveedor(request):
    data = {
        'form': NuevoUserCreationForm(),
        'form2': AddProveedor()
    }

    if request.method == 'POST':
        formulario = NuevoUserCreationForm(data=request.POST)
        formulario2 = AddProveedor(data=request.POST)

        if formulario.is_valid() and formulario2.is_valid():
            
            # Guardamos datos para nuestra base de datos proveedor
            nombre = formulario.cleaned_data['first_name']
            rubro = formulario2.cleaned_data['rubro']
            domicilio = formulario2.cleaned_data['domicilio']
            rut = formulario2.cleaned_data['rut']
            celular = formulario2.cleaned_data['celular']

            formulario.save()
            userProveedor = AuthUser.objects.all().order_by('-id') #Obtiene todos los auth user ordenados descendentemente
            idProveedor = userProveedor[0].id
        
            new_proveedor = Proveedor(nombre = nombre, rut = rut , domicilio = domicilio, celular = celular, rubro = rubro, userid = idProveedor)
            new_proveedor.save()
            return redirect(to='emp_proveedor')
    
        else:
            data["form"] = formulario

    return render(request, 'fermeApp/empleado/addProveedor.html', data)

def modificarProveedor(request, id_prov):

    proveedor = get_object_or_404(Proveedor, id_prov=id_prov)
    data = {
        'form': ModificarProveedor(instance = proveedor)
    }

    if request.method == 'POST':
    
        formulario = ModificarProveedor(data=request.POST, instance=proveedor)
    
        if formulario.is_valid():
            formulario.save()
            return redirect(to= "emp_proveedor")

        data['form'] = formulario

    return render(request, 'fermeApp/empleado/modificarProveedor.html', data)

def eliminar_proveedor(request, id_prov):

    proveedor = get_object_or_404(Proveedor, id_prov=id_prov)
    proveedor.habilitado = 0
    idUser = proveedor.userid
    djangoProveedor = get_object_or_404(AuthUser, id=idUser)
    djangoProveedor.is_active = 0

    proveedor.save()
    djangoProveedor.save()
    return redirect(to= "emp_proveedor")
