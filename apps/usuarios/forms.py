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

	def clean_password2(self):
		""" Validacion de contrasena
			
		Metodo que valida que ambas contrasenas ingresadas sean igual, esto antes de ser encriptadas y guardadas en la base de datos, Retorna la contrasena valida.

		Excepcoiones:
		- ValidationError -- cuando las contrasenas no son iguales muetra un mensaje de error
		"""	

		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('Contrasenas no coinciden!')
		return password2

	def save(self, commit = True):
		user = super().save(commit = False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user