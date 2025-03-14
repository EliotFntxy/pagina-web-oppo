from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('powerbi')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('powerbi')
        else:
            return render(request, 'usuarios/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'usuarios/login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

@login_required
def powerbi(request):
    powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiYjE1YzEyMjktZTFmMC00MTczLTk5YjgtZTE1YzFmM2E2Y2I4IiwidCI6ImY5NGJmNGQ5LTgwOTctNDc5NC1hZGY2LWE1NDY2Y2EyODU2MyIsImMiOjR9"
    return render(request, 'usuarios/powerbi.html', {'powerbi_url': powerbi_url})


def login_view(request):
    return render(request, 'usuarios/login.html')

"""""
@login_required
def acceso_powerbi(request):
    # URL del documento de Power BI (puede ser dinámico o estático)
    powerbi_url = 'https://app.powerbi.com/view?r=eyJrIjoiYjE1YzEyMjktZTFmMC00MTczLTk5YjgtZTE1YzFmM2E2Y2I4IiwidCI6ImY5NGJmNGQ5LTgwOTctNDc5NC1hZGY2LWE1NDY2Y2EyODU2MyIsImMiOjR9'  # Reemplaza con la URL correcta de tu documento Power BI
    
    # Retornar la plantilla con el contexto para la URL
    return render(request, 'documento_powerbi.html', {'powerbi_url': powerbi_url})"
"""