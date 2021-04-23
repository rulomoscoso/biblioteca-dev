from django import forms
from django.contrib.auth.forms import AuthenticationForm
from apps.usuarios.models import Usuario

class FormularioLogin(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(FormularioLogin, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
		self.fields['password'].widget.attrs['class'] = 'form-control'
		self.fields['password'].widget.attrs['placeholder'] = 'Contrasena'


class FormularioUsuario(forms.ModelForm):
	""" Formulario de registro de un susuario en la base de datos

		variables:
			- password1: Contrasena
			- password2: Verificacion de la contrasena
	"""

	password1 = forms.CharField(label='contrasena', widget=forms.PasswordInput(
			attrs = {
				'class': 'form-control',
				'placeholder': 'ingrese su contrasena...',
				'id': 'password1',
				'required': 'required',
			}
		))

	password2 = forms.CharField(label='contrasena de confirmacion', widget=forms.PasswordInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'ingrese nuevamente su contrasena...',
				'id': 'password2',
				'required': 'required',
			}
		))

	class Meta:
		model = Usuario
		fields = ('email', 'username', 'nombres', 'apellidos')
		widgets = {
			'email' : forms.EmailInput(
					attrs = {
						'class' :'form-control',
						'placeholder' : 'Correo Electronico'
					}
				),
			'nombres' : forms.TextInput(
					attrs = {
						'class' : 'form-control',
						'placeholder' : 'Ingrese su nombre'
					}
				),
			'apellidos' : forms.TextInput(
					attrs = {
						'class' : 'form-control',
						'placeholder' : 'Ingrese sus apellidos'
					}
				),
			'username' : forms.TextInput(
					attrs = {
						'class' : 'form-control',
						'placeholder' : 'Ingrese su nombre de usuario'
					}
				)
		}	