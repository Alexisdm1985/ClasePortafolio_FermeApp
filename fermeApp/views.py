from .models import AuthUser, InvProducto, OrdenCompra, Proveedor, FamProducto
from .forms import AddDetalleOrden, AddOrden, NuevoUserCreationForm, AddProducto, AddProveedor, ModificarProveedor
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required, login_required

# Create your views here.


# Global
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
    
# Cliente
# Vendedor
# Empleado
def empleado(request):

    userName = request.user.get_short_name()

    data = {
        'uName': userName if userName else 'Admin'
    }
    return render(request, 'fermeApp/empleado/home.html', data)

# Listar productos
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
        formulario = AddProducto(data=request.POST)

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
    return redirect(to= "homeEmp")

def emp_orden(request):
    orden = OrdenCompra.objects.all()
    data = {
        'ordenes': orden
    }
    return render(request, 'fermeApp/empleado/emp_orden.html', data)

def addOrden(request):
    data = {
        'form': AddOrden(),
        'form2': AddDetalleOrden()
    }

    if request.method == 'POST':
        formulario = AddOrden(data=request.POST)
        formulario2 = AddDetalleOrden(data=request.POST)

        if formulario.is_valid() and formulario2.is_valid():
            formulario.save()
            formulario2.save()

            return redirect(to='emp_proveedor')
            
            # Rescato el nombre del primer formulario
            # prov_nombre = formulario.cleaned_data["first name"]
            # formulario2 += prov_nombre
            # formulario2.save()
            
        else:
            data["form"] = formulario

    return render(request, 'fermeApp/empleado/addOrden.html', data)
# Proveedor
def emp_proveedor(request):
    
    proveedor = Proveedor.objects.all()
    djProveedor = AuthUser.objects.all()

    data = {
        'proveedores': proveedor,
        'djProveedores': djProveedor
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

            new_proveedor = Proveedor(nombre = nombre, rut = rut , domicilio = domicilio, celular = celular, rubro = rubro)

            formulario.save()
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

# def eliminar_proveedor(request, id):
