import json
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, HttpResponse
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

	def get(self, request, *args, **kwargs):
		if request.is_ajax():
			lista_usuarios = []
			for usuario in self.get_queryset():
				data_usuario = {}
				data_usuario['id'] = usuario.id
				data_usuario['nombres'] = usuario.nombres
				data_usuario['apellidos'] = usuario.apellidos
				data_usuario['email'] = usuario.email
				data_usuario['username'] = usuario.username
				data_usuario['usuario_activo'] = usuario.usuario_activo
				lista_usuarios.append(data_usuario)
			data = json.dumps(lista_usuarios)
			#return render(request, self.template_name)
			return HttpResponse(data, 'application/json')
		else:
			return render(request, self.template_name)


class RegistrarUsuario(CreateView):
	model = Usuario
	form_class = FormularioUsuario
	template_name = 'usuarios/crear_usuario.html'
	success_url = reverse_lazy('usuarios:listar_usuarios')

	def post(self, request, *args, **kwargs):
			form = self.form_class(request.POST)
			if form.is_valid():
				nuevo_usuario = Usuario(
					email = form.cleaned_data['email'],
					username = form.cleaned_data['username'],
					nombres = form.cleaned_data['nombres'],
					apellidos = form.cleaned_data['apellidos']
				)
				nuevo_usuario.set_password(form.cleaned_data.get('password1'))
				nuevo_usuario.save()
				return redirect('usuarios:listar_usuarios')
			else:
				return render(reques, self.template_name, {'form':form}) 