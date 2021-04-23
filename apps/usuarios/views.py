from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.usuarios.models import Usuario
from .forms import FormularioLogin, FormularioUsuario
# Create your views here.


class Login(FormView):
	template_name = 'login.html'
	form_class = FormularioLogin
	success_url = reverse_lazy('index')

	@method_decorator(csrf_protect)
	@method_decorator(never_cache)
	def dispatch(self, request  , *args, **kwargs):
		if request.user.is_authenticated:
			return HttpResponseRedirect(self.get_success_url())
		else:
			return super(Login, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		login(self.request, form.get_user())
		return super(Login, self).form_valid(form)
 
def logoutUsuario(request):
 	logout(request)
 	return HttpResponseRedirect('/accounts/login/')

class ListadoUsuarios(ListView):
	model = Usuario
	template_name = 'usuarios/listar_usuario.html'
	#queryset = Usuario.objects.filter(usuario_activo=True)
	def get_queryset(self):
		return self.model.objects.filter(usuario_activo=True)


class RegistrarUsuario(CreateView):
	model = Usuario
	form_class = FormularioUsuario
	template_name = 'usuarios/crear_usuario.html'
	success_url = reverse_lazy('usuarios:listar_usuarios')