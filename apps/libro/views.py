from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import AutorForm, LibroForm
from .models import Autor, Libro
# Create your views here.



class Inicio(TemplateView):
	template_name = 'index.html'


class CrearAutor(CreateView):
	model = Autor
	form_class = AutorForm
	template_name = 'libro/autor/crear_autor.html'
	success_url = reverse_lazy ('libro:listar_autor')


class ListadoAutor(ListView):
	model = Autor
	template_name = 'libro/autor/lista_autores.html'
	context_object_name = 'autores'
	queryset = Autor.objects.filter(status = True)

	"""def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return render(self.template_name)
		else:
			return redirect('login')"""


class ActualizarAutor(UpdateView):
	model = Autor
	template_name = 'libro/autor/crear_autor.html'
	form_class = AutorForm
	success_url = reverse_lazy('libro:listar_autor')


class EliminarAutor(DeleteView):
	model = Autor

	def post(self, request, pk, *args, **kwargs):
		object = Autor.objects.get(id=pk)
		object.status = False
		object.save()
		return redirect('libro:listar_autor')


class ListadoLibro(ListView):
	model = Libro
	template_name = 'libro/libro/listar_libros.html'
	queryset = Libro.objects.filter(status = True) 

class CrearLibro(CreateView):
	model = Libro
	form_class = LibroForm
	template_name = 'libro/libro/crear_libro.html'
	success_url = reverse_lazy('libro:listado_libros')

class ActualizarLibro(UpdateView):
	model = Libro
	template_name = 'libro/libro/crear_libro.html'
	form_class = LibroForm
	success_url = reverse_lazy('libro:listado_libros')

class EliminarLibro(DeleteView):
	model = Libro

	def post(self, request, pk, *args, **kwargs):
		object = Libro.objects.get(id=pk)
		object.status = False
		object.save()
		return redirect('libro:listado_libros')