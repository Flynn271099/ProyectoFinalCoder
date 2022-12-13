from django.urls import path
from Mi_Blog import views

urlpatterns = [
    path('', views.index, name='/'),
    path('C_Empleado/', views.C_Empleado, name='Nuevo Empleado'),
    path('C_jefe/', views.C_Jefe, name='Nuevo Jefe'),
    path('C_Cliente/', views.C_Cliente, name='Nuevo Cliente'),
    path('buscar_cliente/', views.buscar_cliente, name='Buscar Cliente'),
    path('singup/', views.SingUpView.as_view(), name='Sing Up'),
    path('login/', views.AdminLoginView.as_view(), name='Login'),
    path('logouy/', views.AdminLogoutView.as_view(), name='Logout'),
    path('editar_usuario/', views.editar_usuario, name= 'Editar Usuario'),
    path('mostrar_empleados/', views.mostrar_empleados, name= 'Mostrar Empleados'),
    path('elim_empleado/<empleado_id>', views.elim_empleado, name= 'Eliminar Empleado'),
    path('act_empleado/<empleado_id>', views.act_empleado, name='Actualizar Empleado'),
    path('empleado_list/', views.EmpleadoList.as_view(), name='List'),
    path('empleado_detail/<pk>', views.EmpleadoDetailView.as_view(), name='Detail'),
    path('empleado_confirm_delete/<pk>', views.EmpleadoDeleteView.as_view(), name= 'Delete'),
    path('empleado_edit/<pk>', views.EmpleadoUpdateView.as_view(), name= 'Update'),
    path('empleado_form/', views.EmpleadoCreateView.as_view(), name= 'Create'),
    path('jefe_list/', views.JefeList.as_view(), name='ListJefe'),
    path('jefe_detail/<pk>', views.JefeDetailView.as_view(), name='DetailJefe'),
    path('jefe_confirm_delete/<pk>', views.JefeDeleteView.as_view(), name= 'DeleteJefe'),
    path('jefe_edit/<pk>', views.JefeUpdateView.as_view(), name= 'UpdateJefe'),
    path('jefe_form/', views.JefeCreateView.as_view(), name= 'CreateJefe'),
    path('informacion/', views.sobre_mi, name= 'Sobre Mí'),
    
]