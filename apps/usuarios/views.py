import json
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
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
	
	#queryset = Usuario.objects.filter(usuario_activo=True)
	def get_queryset(self):
		return self.model.objects.filter(usuario_activo=True)

	def get(self, request, *args, **kwargs):
		if request.is_ajax():
			data = serialize('json', self.get_queryset())
			return HttpResponse(data, 'application/json')
		else:
			return redirect('usuarios:inicio_usuarios')


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