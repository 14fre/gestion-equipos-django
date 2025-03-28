from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Equipo, ReporteDanio
from .forms import EquipoForm, ReporteDanioForm, RegistroForm

@login_required
def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'reportes/lista_equipos.html', {'equipos': equipos})

@login_required
def registrar_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_equipos')
    else:
        form = EquipoForm()
    return render(request, 'reportes/registrar_equipo.html', {'form': form})

@login_required
def editar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    if request.method == 'POST':
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('lista_equipos')
    else:
        form = EquipoForm(instance=equipo)
    return render(request, 'reportes/editar_equipo.html', {'form': form, 'equipo': equipo})

@login_required
def eliminar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    if request.method == 'POST':
        equipo.delete()
        return redirect('lista_equipos')
    return render(request, 'reportes/eliminar_equipo.html', {'equipo': equipo})

@login_required
def reportar_danio(request):
    if request.method == 'POST':
        form = ReporteDanioForm(request.POST)
        if form.is_valid():
            reporte = form.save()
            if reporte.estado == 'BAJA':
                reporte.equipo.activo = False
                reporte.equipo.save()
            return redirect('lista_equipos')
    else:
        form = ReporteDanioForm()
    return render(request, 'reportes/reportar_danio.html', {'form': form})

@login_required
def detalle_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    reportes = ReporteDanio.objects.filter(equipo=equipo)
    return render(request, 'reportes/detalle_equipo.html', {'equipo': equipo, 'reportes': reportes})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guardar el usuario en la base de datos
            login(request, user)  # Loguear al usuario automáticamente
            return redirect('lista_equipos')  # Redirigir a la lista de equipos
        else:
            print(form.errors)  # Imprimir errores en la consola para depurar
    else:
        form = RegistroForm()
    return render(request, 'reportes/registro.html', {'form': form})