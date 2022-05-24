from email.policy import default
from .models import AuthUser, DetalleOrden, InvProducto, OrdenCompra, Proveedor, FamProducto, TipoProducto
from .forms import AddDetalleOrden, AddOrden, ModificarIdProveedor, NuevoUserCreationForm, AddProducto, AddProveedor, ModificarProveedor, AddDetalle, ModificarProducto
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages

# Create your views here.

# GLOBAL
def index(request):
    
    # Obtiene todos los productos
    listadoProducto = InvProducto.objects.filter(habilitado=1)
    data = {
        'productos': listadoProducto
        
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
    producto = InvProducto.objects.filter(habilitado=1)
    # categorias = ['Herramientas', 'Gasfiteria', 'Hogar', 'Construccion']
    data = {
        # 'categorias': categorias,
        'productos': producto
    }

    if request.POST.get('nombre'):
        tituloAfiltrar = request.POST.get('nombre')
        producto = producto.filter(nombre__icontains=tituloAfiltrar)

    return render(request, 'fermeApp/productos.html', {'productos':producto})

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

    # producto = InvProducto.objects.filter(habilitado=1) # Filtra todos los productos con habilitado=1
    # data = {
    #     'productos': producto
    # }

    if request.POST.get('nombre'):
        tituloAfiltrar = request.POST.get('nombre')
        producto = producto.filter(nombre__icontains=tituloAfiltrar, habilitado=1)

    return render(request, 'fermeApp/empleado/emp_productos.html', {'productos': producto})
# @permission_required('fermeApp.add_invproducto')
def addProducto(request):
    
    data = {
        'form': AddProducto(),
        'proveedor': ModificarIdProveedor()
    }

    if request.method == 'POST':
        formulario = AddProducto(data=request.POST, files=request.FILES)
        
        formProveedor = ModificarIdProveedor(data=request.POST) # Obtiene el id del proveedor seleccionado

        if formulario.is_valid() and formProveedor.is_valid():

            # fecha = formulario.cleaned_data['fecha_venc']
            # formulario.cleaned_data['fecha_venc'] = fecha.strip() # Elimino cualquier espacio

            producto = InvProducto()
            producto = formulario.cleaned_data # Lleno el objeto con el formulario

            # Obtengo id_prod en base a proveedor id - familia - fechaVenc - tipo
            proveedor = Proveedor.objects.get(id_prov = formProveedor.cleaned_data['proveedor_id_prov'])
            
            familia = formulario.cleaned_data['fam_producto_id_fam']
            id_fam = FamProducto.objects.get(descripcion=familia )

            tipo = formulario.cleaned_data['tipo_producto_id_tipo']
            id_tipo = TipoProducto.objects.get(descripcion=tipo)

            fecha_form = formulario.cleaned_data['fecha_venc']
            id_producto = 0

            if fecha_form is None:
                fecha_form = "00000000"
                id_producto = str(proveedor.id_prov) + str(id_fam.id_fam) + fecha_form + str(id_tipo.id_tipo)
                id_producto = int(id_producto)
                fecha_form = None
            else:
                fecha_form = str(fecha_form).replace("-", "")
                id_producto = str(proveedor.id_prov) + str(id_fam.id_fam) + fecha_form + str(id_tipo.id_tipo)
                id_producto = int(id_producto)
                fecha_form = formulario.cleaned_data['fecha_venc']
            
            
            new_producto = InvProducto(id_prod=id_producto, nombre= producto['nombre'], precio=producto['precio'], stock=producto['stock'], stock_crit=producto['stock_crit'] ,stock_max=producto['stock_max'], fecha_venc = fecha_form, fam_producto_id_fam = producto['fam_producto_id_fam'], marca = producto['marca'], tipo_producto_id_tipo = producto['tipo_producto_id_tipo'], categoria = producto['categoria']) 
            new_producto.save()
            
            # return redirect(to='emp_productos')
        data["form"] = formulario

    return render(request, 'fermeApp/empleado/addProducto.html', data)

def modificarProducto(request, id):

    producto = get_object_or_404(InvProducto, id_prod=id)

    data = {
        'form': ModificarProducto(instance = producto)
    }

    if request.method == 'POST':
        # En data no viene el id pero si esta en la instancia de producto
        formulario = ModificarProducto(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()

            messages.success(request, "Producto modificado satisfactoriamente") 
            return redirect(to= "emp_productos")

        data['form'] = formulario

    return render(request, 'fermeApp/empleado/modificarProducto.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(InvProducto, id_prod=id)
    producto.habilitado = 0
    producto.save()

    messages.success(request, "Producto eliminado satisfactoriamente") 
    return redirect(to= "emp_productos")

# ORDEN COMPRA
def emp_orden(request):
    orden = OrdenCompra.objects.all()
    # idProveedor = []

    # for i in orden: # Obtiene el id_proveedor de cada orden
    #     detalles = DetalleOrden.objects.filter(orden_compra_nro_orden=i.nro_orden)
    #     idProveedor.append(detalles[0].proveedor_id_prov)

    data = {
        'ordenes': orden
        # 'id_prov': idProveedor
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
        
            orden = new_orden[0].nro_orden  #Obtiene la ultima orden de compra ingresada
            ordenInstance = OrdenCompra.objects.get(nro_orden = orden)
            
            detalle_orden = DetalleOrden(orden_compra_nro_orden= ordenInstance, proveedor_id_prov = id_prov, cantidad = cantidad, precio = precio, descuento= descuento, observaciones = observaciones, nombre = nombre)
            detalle_orden.save()

            messages.success(request, "Su orden ha sido ingresada correctamente") 
            return redirect(to='emp_orden')
            
        else:
            data["form"] = formulario

    return render(request, 'fermeApp/empleado/addOrden.html', data)

def addDetalle(request, nro_orden):
    detalles = DetalleOrden.objects.filter(orden_compra_nro_orden=nro_orden)
    orden = OrdenCompra.objects.get(nro_orden=nro_orden)
    proveedor = Proveedor.objects.get(id_prov=detalles[0].proveedor_id_prov)

    data = {
        'form_detalle': AddDetalle()
    }

    if request.method == 'POST':
        formulario = AddDetalle(data=request.POST, instance=detalles[0])
        
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            cantidad = formulario.cleaned_data['cantidad']
            precio = formulario.cleaned_data['precio']
            descuento = formulario.cleaned_data['descuento']
            observaciones = formulario.cleaned_data['observaciones']

            # Crear detalle orden 
            new_detalle = DetalleOrden(orden_compra_nro_orden= orden, proveedor_id_prov= proveedor, cantidad = cantidad, precio=precio, descuento=descuento, observaciones=observaciones, nombre = nombre )
            new_detalle.save()

            messages.success(request, "Detalle de orden agregada correctamente") 
            return redirect(to= 'emp_orden')          

        data['form_detalle'] = formulario

    return render(request, 'fermeApp/empleado/addDetalleOrden.html', data)

def modificarOrden(request, nro_orden):

    ordenCompra = get_object_or_404(OrdenCompra, nro_orden=nro_orden)
    detalleOrden = DetalleOrden.objects.filter(orden_compra_nro_orden = nro_orden) # Todos sus detalles

    data = {
        'form': AddOrden(instance = ordenCompra),
        'id_prov_form': ModificarIdProveedor()
    }

    if request.method == 'POST':

        formulario = AddOrden(data=request.POST, instance=ordenCompra) # Contiene los datos de orden compra seleccionados
        formularioDetalle = ModificarIdProveedor(data=request.POST) # Contiene el id proveedor seleccionado

        if formularioDetalle.is_valid() and formulario.is_valid():

            proveedor = Proveedor.objects.get(id_prov = formularioDetalle.cleaned_data['proveedor_id_prov']) #Obtiene instancia proveedor
            formulario.save()

            for i in detalleOrden: # Itero cada detalle para modificar id proveedor

                i.proveedor_id_prov = proveedor
                i.save()

            messages.success(request, "Orden de compra modificada correctamente") 
            return redirect(to= "emp_orden")

        else: print("Error views.py def modificarOrden")

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

            messages.success(request, "Detalle de orden modificada correctamente") 
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

            messages.success(request, "Proveedor agregado satisfactoriamente") 
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

            nombre = formulario.cleaned_data['nombre']
            authProveedor = AuthUser.objects.get(id = proveedor.userid)
            authProveedor.first_name = nombre
            authProveedor.save()
            formulario.save()

            messages.success(request, "Proveedor modificado correctamente") 
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

    messages.success(request, "Proveedor eliminado satisfactoriamente") 
    return redirect(to= "emp_proveedor")
