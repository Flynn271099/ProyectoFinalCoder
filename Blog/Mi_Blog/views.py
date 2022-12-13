from django.shortcuts import render
from Mi_Blog.models import *
from Mi_Blog.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


#Redirección
from django.urls import reverse_lazy
# Auth
from django.contrib.auth.views import LoginView, LogoutView
#Los decoradores sirven para funciones > vistas basadas en funciones
from django.contrib.auth.decorators import login_required

#ejemplo
# @decorador
# def funcion_a_proteger

#Los mixins sirven para clases > vistas basadas en clases
from django.contrib.auth.mixins import LoginRequiredMixin

#ejemplo
# class ClaseAProteger(MixinParaProteger)

# Create your views here.
def index(request):
    if request.user.is_authenticated == True:
        imagenes = Avatar.objects.filter(user=request.user.id)
            
        return render(request, 'Mi_Blog/index.html', {'url': imagenes[0].imagen.url})
    
    else:
        return render(request, 'Mi_Blog/index.html')

def sobre_mi(request):
    
        return render(request, 'Mi_Blog/sobre_mi.html')

@login_required
def C_Empleado(request):
        
    formulario = AniadirEmpleado()
    
    if request.method == "POST":
        
        formulario = AniadirEmpleado(request.POST)
        
        if formulario.is_valid():
            
            formulario_limpio = formulario.cleaned_data
        
            empleado = Empleado(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], sueldo=formulario_limpio['sueldo'], email=formulario_limpio['email'])
            
            empleado.save()

            return render(request, 'Mi_Blog/index.html')
    
    else:
        formulario = AniadirEmpleado()
    
    return render(request, 'Mi_Blog/empleado.html', {'formulario': AniadirEmpleado})

def mostrar_empleados(request):
    
    empleados = Empleado.objects.all()
    
    context = {'empleados': empleados}
    
    return render(request, 'Mi_Blog/mostrar_empleados.html', context=context)

def elim_empleado(request, empleado_id):
    
    empleado = Empleado.objects.get(id=empleado_id)
    
    empleado.delete()
    
    empleados = Empleado.objects.all()
    
    context = {'empleados': empleados}
    
    return render(request, 'Mi_Blog/mostrar_empleados.html', context=context)

def act_empleado(request, empleado_id):
        
    empleado = Empleado.objects.get(id=empleado_id)
    
    if request.method == "POST":
        
        formulario = AniadirEmpleado(request.POST)
        
        if formulario.is_valid():
            
            formulario_limpio = formulario.cleaned_data
        
            empleado.nombre = formulario_limpio['nombre']
            empleado.apellido = formulario_limpio['apellido']
            empleado.email = formulario_limpio['email']
            empleado.profesion = formulario_limpio['profesion']
            
            empleado.save()

            return render(request, 'Mi_Blog/index.html')
    
    else:
        formulario = AniadirEmpleado(initial={'nombre': empleado.nombre, 'apellido': empleado.apellido, 'email': empleado.email, 'sueldo': empleado.sueldo})
    
    return render(request, 'Mi_Blog/actualizar_empleado.html', {'formulario': AniadirEmpleado, 'empleado': empleado})

@login_required
def C_Jefe(request):
        
    formulario = AniadirJefe()
    
    if request.method == "POST":
        
        formulario = AniadirJefe(request.POST)
        
        if formulario.is_valid():
            
            formulario_limpio = formulario.cleaned_data
        
            jefe = Jefe(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], sueldo=formulario_limpio['sueldo'], email=formulario_limpio['email'])
            
            jefe.save()

            return render(request, 'Mi_Blog/index.html')
    
    else:
        formulario = AniadirJefe()
    
    return render(request, 'Mi_Blog/jefe.html', {'formulario': AniadirJefe})

@login_required
def C_Cliente(request):
        
    formulario = AniadirCliente()
    
    if request.method == "POST":
        
        formulario = AniadirCliente(request.POST)
        
        if formulario.is_valid():
            
            formulario_limpio = formulario.cleaned_data
        
            cliente = Cliente(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], email=formulario_limpio['email'])
            
            cliente.save()

            return render(request, 'Mi_Blog/index.html')
    
    else:
        formulario = AniadirCliente()
    
    return render(request, 'Mi_Blog/cliente.html', {'formulario': AniadirCliente})

@login_required
def buscar_cliente(request):
    
    if request.GET.get('email', False):
        
        email = request.GET['email']
        clientes = Cliente.objects.filter(email__icontains=email)
        
        return render(request, 'Mi_Blog/buscar_cliente.html', {'clientes': clientes})
    else:
        
        respuesta = 'No hay datos.'
    
    return render(request, 'Mi_Blog/buscar_cliente.html', {'respuesta': respuesta})

@login_required
def editar_usuario(request):
    
    usuario = request.user
    
    if request.method == 'POST':
        usuario_form = UserEditForm(request.POST)
        
        
        if usuario_form.is_valid():
    
            informacion = usuario_form.cleaned_data
            
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            
            usuario.save()
            
            return render(request, 'Mi_Blog/index.html')

    else:
        usuario_form = UserEditForm(initial={
            'username': usuario.username,
            'email': usuario.email,
            })
    return render(request, 'Mi_Blog/admin_update.html', {
        'form': usuario_form,
        'usuario': usuario,
    })

class EmpleadoList(LoginRequiredMixin, ListView):
    
    model = Empleado
    template_name = 'Mi_Blog/empleado_list.html'

class EmpleadoDetailView(DetailView):
    
    model = Empleado
    template_name = 'Mi_Blog/empleado_detalle.html'
    
    
class EmpleadoDeleteView(DeleteView):
    
    model = Empleado
    success_url = '/empleado_list'
    
class EmpleadoDeleteView(DeleteView):
    
    #Recordatorio, en succes_url utilizar el nombre de la url
    #Ejemplo:
    #path('curso_list', views.CursoList.as_view(), name= 'List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de un / (slash) ""
    model = Empleado
    success_url = '/empleado_list'
    
class EmpleadoUpdateView(UpdateView):
    
    #Recordatorio, en succes_url utilizar el nombre de la url
    #Ejemplo:
    #path('curso_list', views.CursoList.as_view(), name= 'List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de un / (slash) ""
    model = Empleado
    success_url = '/empleado_list'
    fields = ['nombre', 'apellido', 'email', 'sueldo']
    
class EmpleadoCreateView(CreateView):
    
    #Recordatorio, en succes_url utilizar el nombre de la url
    #Ejemplo:
    #path('curso_list', views.CursoList.as_view(), name= 'List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de un / (slash) ""
    model = Empleado
    success_url = '/empleado_list'
    fields = ['nombre', 'apellido', 'email', 'sueldo']
    
class JefeList(LoginRequiredMixin, ListView):
    
    model = Jefe
    template_name = 'Mi_Blog/jefe_list.html'

class JefeDetailView(DetailView):
    
    model = Jefe
    template_name = 'Mi_Blog/jefe_detalle.html'
    
    
class JefeDeleteView(DeleteView):
    
    model = Jefe
    success_url = '/jefe_list'
    
class JefeDeleteView(DeleteView):
    
    #Recordatorio, en succes_url utilizar el nombre de la url
    #Ejemplo:
    #path('curso_list', views.CursoList.as_view(), name= 'List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de un / (slash) ""
    model = Jefe
    success_url = '/jefe_list'
    
class JefeUpdateView(UpdateView):
    
    #Recordatorio, en succes_url utilizar el nombre de la url
    #Ejemplo:
    #path('curso_list', views.CursoList.as_view(), name= 'List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de un / (slash) ""
    model = Jefe
    success_url = '/jefe_list'
    fields = ['nombre', 'apellido', 'email', 'sueldo']
    
class JefeCreateView(CreateView):
    
    #Recordatorio, en succes_url utilizar el nombre de la url
    #Ejemplo:
    #path('curso_list', views.CursoList.as_view(), name= 'List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de un / (slash) ""
    model = Jefe
    success_url = '/jefe_list'
    fields = ['nombre', 'apellido', 'email', 'sueldo']

class SingUpView(CreateView):
    
    #Recordatorio, en succes_url utilizar el nombre de la url
    #Ejemplo:
    #path('curso_list', views.CursoList.as_view(), name= 'List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de un / (slash) ""
    form_class = SingUpForm
    success_url = reverse_lazy('/')
    template_name = 'Mi_Blog/registro.html'


class AdminLoginView(LoginView):
    
    template_name = 'Mi_Blog/login.html'
    
class AdminLogoutView(LogoutView):
    
    template_name = 'Mi_Blog/logout.html'