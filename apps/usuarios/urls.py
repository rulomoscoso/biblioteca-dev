from django.urls import path
from django.contrib.auth.decorators import login_required
from .views  import ListadoUsuarios, RegistrarUsuario

urlpatterns = [
	path('listado_usuarios/', login_required(ListadoUsuarios.as_view()), name = 'listar_usuarios'),
	path('registrar_usuario/', login_required(RegistrarUsuario.as_view()), name='registrar_usuario')
]