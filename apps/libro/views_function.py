#def home(request):
# 	return render(request, 'libro/index.html',{ 'context': 'Hola Mundo'})

"""
	1.- dispatch(): valida la peticion y elige que metodo HTTP se utilizo para la solicitud
	2.- http_method_not_allowed(): retorna un error cuando se utiliza un metodo HTTP no soportado o definido
	3.- options()
"""


"""def crearAutor(request):
	if request.method == 'POST':
		 
		autor_form  = AutorForm(request.POST)
		if autor_form.is_valid():
			autor_form.save()
			return redirect('libro:listar_autor')

	else:
		autor_form = AutorForm()
		print(autor_form)
	return render(request, 'libro/crear_autor.html', {'autor_form': autor_form})"""


"""def listaAutor(request):
	autores = Autor.objects.filter(status = True)
	return render(request, 'libro/lista_autores.html', {'autores':autores})"""



"""def editarAutor(request, id):
	autor_form = None
	error = None
	try:
		autor = Autor.objects.get(id = id)
		if request.method == 'GET':
			autor_form = AutorForm(instance = autor)
		else:
			autor_form = AutorForm(request.POST, instance = autor)
			if autor_form.is_valid():
				autor_form.save()
				return redirect('libro:listar_autor')
	except ObjectDoesNotExist as e:
		error = e
	
	return render(request, 'libro/crear_autor.html', {'autor_form': autor_form, 'error': error} )"""


"""def eliminarAutor(request, id):
	autor = Autor.objects.get(id = id)
	if request.method == 'POST':		
		#autor.delete() //Eliminacion directa de la BD
		autor.estado = False #Eliminacion logica cambiar el campo status
		autor.save()
		return redirect('libro:listar_autor')
	return render(request, 'libro/eliminar_autor.html', {'autor': autor})"""