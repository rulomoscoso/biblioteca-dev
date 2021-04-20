from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View, TemplateView, ListView, CreateView, DeleteView
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


class ListadoAutor(View):
	model = Autor
	form_class = AutorForm
	template_name = 'libro/autor/lista_autores.html'

	def get_queryset(self):
		return self.model.objects.filter(status=True)

	def get_context_data(self, *args, **kwargs):
		contexto = {}
		contexto['autores'] = self.get_queryset()
		contexto['form'] = self.form_class
		return contexto

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, self.get_context_data())


class ActualizarAutor(UpdateView):
	model = Autor
	template_name = 'libro/autor/autor.html'
	form_class = AutorForm
	success_url = reverse_lazy('libro:listar_autor')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['autores'] = Autor.objects.filter(status=True)
		return context


class EliminarAutor(DeleteView):
	model = Autor

	def post(self, request, pk, *args, **kwargs):
		object = Autor.objects.get(id=pk)
		object.status = False
		object.save()
		return redirect('libro:listar_autor')




class ListadoLibro(View):
	model = Libro
	form_class = LibroForm
	template_name = 'libro/libro/listar_libros.html'

	def get_queryset(self):
		return self.model.objects.filter(status = True)

	def get_context_data(self, *args, **kwargs):
		contexto = {}
		contexto['libros'] = self.get_queryset()
		contexto['form'] = self.form_class
		return contexto

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, self.get_context_data() )

	"""def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			return redirect('libro:listado_libros')"""


class CrearLibro(CreateView):
	model = Libro
	form_class = LibroForm
	template_name = 'libro/libro/crear_libro.html'
	success_url = reverse_lazy('libro:listado_libros')

class ActualizarLibro(UpdateView):
	model = Libro
	template_name = 'libro/libro/libro.html'
	form_class = LibroForm
	success_url = reverse_lazy('libro:listado_libros')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['libros'] = Libro.objects.filter(status=True)
		return context

class EliminarLibro(DeleteView):
	model = Libro

	def post(self, request, pk, *args, **kwargs):
		object = Libro.objects.get(id=pk)
		object.status = False
		object.save()
		return redirect('libro:listado_libros')