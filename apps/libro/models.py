from django.db import models

# Create your models here.
class Autor(models.Model):
	nombre = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=200)
	nacionalidad = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=200)
	status = models.BooleanField(default=True)
	fecha_creacion = models.DateTimeField(verbose_name='Fecha de creacion', auto_now_add=True)
	fecha_edicion = models.DateTimeField(verbose_name='Fecha de edicion', auto_now=True)

	class Meta:
		verbose_name = 'Autor'
		verbose_name_plural = 'Autores'
		ordering = ['nombre']

	def __str__(self):
		return self.nombre

class Libro(models.Model):
	titulo = models.CharField(max_length=255)
	fecha_publicacion = models.DateField(verbose_name='Fecha de publicacion')
	autor_id = models.ManyToManyField(Autor)
	fecha_creacion = models.DateTimeField(verbose_name='Fecha de creacion', auto_now_add=True)
	fecha_edicion = models.DateTimeField(verbose_name='Fecha de edicion', auto_now=True)
	status = models.BooleanField(default=True, verbose_name='Status')
	class Meta:
		verbose_name='Libro'
		verbose_name_plural = 'Libros'
		ordering = ['titulo']

	def __str__(self):
		return self.titulo