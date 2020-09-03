from django.contrib import admin

from .models import JuegosSerios, Autores, Objetivos, Jugadores, Practicas, Principios, Metricas, Sugerencias


class AutoresInline(admin.StackedInline):
    model = Autores
    extra = 1


class ObjetivosInline(admin.StackedInline):
    model = Objetivos


class JugadoresInline(admin.StackedInline):
    model = Jugadores


class PracticasInline(admin.StackedInline):
    model = Practicas


class PrincipiosInline(admin.StackedInline):
    model = Principios


class MetricasInline(admin.StackedInline):
    model = Metricas


class SugerenciasInline(admin.StackedInline):
    model = Sugerencias


class JuegoSeriosAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['nombre', 'descripcion', 'duracion', 'tipo_actividad', 'licencia', 'complejidad', 'dificultad',
                       'idioma', 'tipo_juego']}),
        ('Enlaces externos', {'fields': ['documentacion', 'manuales', 'video']}),
        ('Pre-requisitos', {'fields': ['pre_requisitos']}),
    ]
    list_display = ('nombre', 'duracion', 'licencia', 'idioma')
    inlines = [AutoresInline,ObjetivosInline, JugadoresInline, PracticasInline, PrincipiosInline, MetricasInline]


class SugerenciasAdmin(admin.ModelAdmin):
    list_display = ('sugerencia', 'experiencia', 'perfil', 'importancia', 'categoria')


# Register your models here.
admin.site.register(JuegosSerios, JuegoSeriosAdmin)
admin.site.register(Sugerencias, SugerenciasAdmin)
admin.site.register(Autores)
admin.site.register(Objetivos)
admin.site.register(Jugadores)
admin.site.register(Practicas)
admin.site.register(Principios)
admin.site.register(Metricas)
