from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views  import ListadoUsuarios, RegistrarUsuario

urlpatterns = [
	path('listado_usuarios/', login_required(ListadoUsuarios.as_view()), name = 'listar_usuarios'),
	path('registrar_usuario/', login_required(RegistrarUsuario.as_view()), name='registrar_usuario')
]

#URL DE VISTAS IMPLICITAS
urlpatterns += [
	path('inicio_usuarios/', login_required(TemplateView.as_view(template_name = 'usuarios/listar_usuario.html' )), name = 'inicio_usuarios'),
]