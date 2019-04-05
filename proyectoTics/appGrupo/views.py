from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'appGrupo/index.html')
def reservas(request):
	return render(request, 'appGrupo/reservas.html')
def servicios(request):
	return render(request, 'appGrupo/servicios.html')
def quienes(request):
	return render(request, 'appGrupo/quienes.html')
def galeria(request):
	return render(request, 'appGrupo/galeria.html')
def contacto(request):
	return render(request, 'appGrupo/contacto.html')