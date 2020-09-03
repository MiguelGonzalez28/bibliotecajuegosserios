from django.shortcuts import get_object_or_404, render
from .models import JuegosSerios, Autores, Objetivos, Jugadores, Practicas, Principios, Metricas, Sugerencias
from .forms import ContactForm, SugerenciasForm
from django.core.mail import send_mail, BadHeaderError


def home(request):
    return render(request, 'index.html')


def juegos_serios(request):
    todos_juegos_serios = JuegosSerios.objects.all()
    autores = Autores.objects.select_related('juego_serio')
    if request.method == 'GET':
        nombre_juego_serio_query = request.GET.get('nombre_juego_serio')
        objetivos_aprendizaje_query = request.GET.getlist('objetivos_aprendizaje')
        duracion_min_query = request.GET.get('duracion_min')
        duracion_max_query = request.GET.get('duracion_max')
        jugadores_min_query = request.GET.get('jugadores_min')
        jugadores_max_query = request.GET.get('jugadores_max')
        complejidad_query = request.GET.get('complejidad')
        dificultad_implementacion_query = request.GET.get('dificultad_implementacion')

        if nombre_juego_serio_query != '' and nombre_juego_serio_query is not None:
            todos_juegos_serios = todos_juegos_serios.filter(nombre__icontains = nombre_juego_serio_query)

        if objetivos_aprendizaje_query != '' and objetivos_aprendizaje_query is not None:
            for objetivo in objetivos_aprendizaje_query:
                if objetivo == 'objetivo_1':
                    todos_juegos_serios = todos_juegos_serios.filter(objetivos__objetivo_1__gt = 0)
                elif objetivo == 'objetivo_2':
                    todos_juegos_serios = todos_juegos_serios.filter(objetivos__objetivo_2__gt = 0)
                elif objetivo == 'objetivo_3':
                    todos_juegos_serios = todos_juegos_serios.filter(objetivos__objetivo_3__gt=0)
                elif objetivo == 'objetivo_4':
                    todos_juegos_serios = todos_juegos_serios.filter(objetivos__objetivo_4__gt=0)
                elif objetivo == 'objetivo_5':
                    todos_juegos_serios = todos_juegos_serios.filter(objetivos__objetivo_5__gt=0)
                elif objetivo == 'objetivo_6':
                    todos_juegos_serios = todos_juegos_serios.filter(objetivos__objetivo_6__gt=0)
                elif objetivo == 'objetivo_7':
                    todos_juegos_serios = todos_juegos_serios.filter(objetivos__objetivo_7__gt=0)

        if duracion_min_query != '' and duracion_min_query is not None:

            duracion_min_query = int(duracion_min_query)

            if duracion_min_query > 1440:
                duracion_min_query = 300

            todos_juegos_serios = todos_juegos_serios.filter(duracion__gte = duracion_min_query)

        if duracion_max_query != '' and duracion_max_query is not None:

            duracion_max_query = int(duracion_max_query)

            if duracion_max_query > 1440:
                duracion_max_query = 300

            todos_juegos_serios = todos_juegos_serios.filter(duracion__lte = duracion_max_query)

        if jugadores_min_query != '' and jugadores_min_query is not None:

            jugadores_min_query = int(jugadores_min_query)

            if jugadores_min_query > 15:
                jugadores_min_query = 15

            todos_juegos_serios = todos_juegos_serios.filter(jugadores__min__gte = jugadores_min_query)

        if jugadores_max_query != '' and jugadores_max_query is not None:

            jugadores_max_query = int(jugadores_max_query)

            if jugadores_max_query > 15:
                jugadores_max_query = 15

            todos_juegos_serios = todos_juegos_serios.filter(jugadores__max__lte = jugadores_max_query)

        if complejidad_query != '' and complejidad_query is not None:
            todos_juegos_serios = todos_juegos_serios.filter(complejidad__iexact = complejidad_query)

        if dificultad_implementacion_query != '' and dificultad_implementacion_query is not None:
            todos_juegos_serios = todos_juegos_serios.filter(dificultad__iexact = dificultad_implementacion_query)

    context = {
        'juegos_serios': todos_juegos_serios,
        'autores': autores,
    }
    return render(request, 'juegos_serios.html', context)


def detalles(request, juego_serio_id):
    juego_serio = get_object_or_404(JuegosSerios, pk=juego_serio_id)
    autores = Autores.objects.filter(juego_serio_id = juego_serio_id)
    jugadores = Jugadores.objects.filter(juego_serio_id = juego_serio_id)
    objetivos = Objetivos.objects.filter(juego_serio_id = juego_serio_id)
    practicas = Practicas.objects.filter(juego_serio_id = juego_serio_id)
    principios = Principios.objects.filter(juego_serio_id = juego_serio_id)
    metricas = Metricas.objects.filter(juego_serio_id = juego_serio_id)

    context = {
        'juego_serio': juego_serio,
        'autores': autores,
        'jugadores': jugadores,
        'objetivos': objetivos,
        'practicas': practicas,
        'principios': principios,
        'metricas': metricas,
    }

    return render(request, 'detalles.html', context)


def sugerencias(request):
    if request.method == 'POST':
        form = SugerenciasForm(request.POST)
        if form.is_valid():
            return render(request, 'sugerencias.html', {'form': form})
    else:
        form = SugerenciasForm()
    return render(request, 'sugerencias.html', {'form': form})


def resultados(request):
    if request.method == 'POST':
        experiencia = request.POST.get('experiencia')
        perfil = request.POST.get('perfil')
        categoria = request.POST.get('categoria')
        if categoria == 'Objetivos de aprendizaje':
            if experiencia != '':
                if perfil != '':
                    sugerencias = Sugerencias.objects.filter(categoria = categoria,
                                                             experiencia = experiencia,
                                                             perfil = perfil).order_by('-importancia')
                    mode = 1
                else:
                    sugerencias = Sugerencias.objects.filter(categoria=categoria,
                                                             experiencia=experiencia).order_by('sugerencia')
                    mode = 2
            else:
                if perfil != '':
                    sugerencias = Sugerencias.objects.filter(categoria=categoria,
                                                             perfil=perfil).order_by('perfil')
                    mode = 3
                else:
                    sugerencias = Sugerencias.objects.filter(categoria=categoria).order_by('experiencia')
                    mode = 4
        elif categoria == 'Juegos serios':
            if experiencia != '':
                sugerencias = Sugerencias.objects.filter(categoria=categoria,
                                                         experiencia=experiencia,
                                                         importancia__gte=1).order_by('-importancia')
                mode = 5
            else:
                sugerencias = Sugerencias.objects.filter(categoria=categoria, importancia__gte=1).order_by('experiencia', '-importancia')
                mode = 6
        else:
            if experiencia != '':
                sugerencias = Sugerencias.objects.filter(categoria=categoria,
                                                         experiencia=experiencia,
                                                         importancia__gte=1).order_by('-importancia')
                mode = 5
            else:
                sugerencias = Sugerencias.objects.filter(categoria=categoria, importancia__gte=1).order_by('experiencia', '-importancia')
                mode = 6
    context = {
        'sugerencias': sugerencias,
        'categoria': categoria,
        'experiencia': experiencia,
        'perfil': perfil,
        'mode': mode
    }
    return render(request, 'resultados.html', context)


def contactanos(request):
    success = False
    sending_message = ""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                # send email code goes here
                sender_name = form.cleaned_data['nombre']
                sender_email = form.cleaned_data['email']

                message = "{0} te ha enviado un nuevo mensaje:\n\n{1}\n\n{2}".format(sender_name, form.cleaned_data['mensaje'], sender_email)
                send_mail('Mensaje del sitio de la Biblioteca', message, sender_email, ['miguel.gonzalez@cimat.mx'])
                success = True
                sending_message = "¡Mensaje enviado correctamente!"
            except BadHeaderError:
                sending_message = "Se enonctró un error en el encabezado."
    else:
        form = ContactForm()

    context = {
        'form': form,
        'success': success,
        'message': sending_message,
    }
    return render(request, 'contactanos.html', context)