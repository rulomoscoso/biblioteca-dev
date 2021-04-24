from django.urls import path
from django.contrib.auth.decorators import login_required
from .views  import ListadoUsuarios, RegistrarUsuario, InicioListadoUsuario

urlpatterns = [
	path('inicio_usuarios/', login_required(InicioListadoUsuario.as_view()), name = 'inicio_usuarios'),
	path('listado_usuarios/', login_required(ListadoUsuarios.as_view()), name = 'listar_usuarios'),
	path('registrar_usuario/', login_required(RegistrarUsuario.as_view()), name='registrar_usuario')
]