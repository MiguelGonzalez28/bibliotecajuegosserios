from django.db import models


class JuegosSerios(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    duracion = models.IntegerField(null=True, blank=True, default=0)

    JUEGO_SERIO = 'Juego Serio'
    JUEGO_SIMULACION = 'Juego de Simulacion'
    TIPO_ACTIVIDAD_CHOICES = [
        (JUEGO_SERIO, 'Juego Serio'),
        (JUEGO_SIMULACION, 'Juego de Simulación'),
    ]
    tipo_actividad = models.CharField(
        max_length=20,
        choices=TIPO_ACTIVIDAD_CHOICES,
        null=True,
        blank=True
    )

    licencia = models.CharField(max_length=100, null=True, blank=True)
    documentacion = models.URLField(null=True, blank=True)

    BAJA = 'Baja'
    MEDIA = 'Media'
    ALTA = 'Alta'
    COMPLEJIDAD_Y_DIFICULTAD_CHOICES = [
        (BAJA, 'Baja'),
        (MEDIA, 'Media'),
        (ALTA, 'Alta'),
    ]
    complejidad = models.CharField(
        max_length=5,
        choices=COMPLEJIDAD_Y_DIFICULTAD_CHOICES,
        null=True,
        blank=True
    )
    dificultad = models.CharField(
        max_length=5,
        choices=COMPLEJIDAD_Y_DIFICULTAD_CHOICES,
        null=True,
        blank=True
    )

    manuales = models.URLField(null=True, blank=True)
    video = models.URLField(null=True, blank=True)

    SPANISH = 'Español'
    INGLES = 'Inglés'
    FRANCES = 'Francés'
    PORTUGUES = 'Portugués'
    OTHER = 'Otro'
    IDIOMA_CHOICES = [
        (SPANISH, 'Español'),
        (INGLES, 'Ingles'),
        (FRANCES, 'Frances'),
        (PORTUGUES, 'Portugues'),
        (OTHER, 'Otro'),
    ]
    idioma = models.CharField(
        max_length=10,
        choices=IDIOMA_CHOICES,
        null=True,
        blank=True
    )

    pre_requisitos = models.TextField(null=True, blank=True)

    COOPERATIVO = 'Cooperativo'
    COMPETITIVO = 'Competitivo'
    AMBOS = 'Cooperativo/Competitivo'
    TIPO_JUEGO_CHOICES = [
        (COOPERATIVO, 'Cooperativo'),
        (COMPETITIVO, 'Competitivo'),
        (AMBOS, 'Cooperativo/Competitivo'),
    ]
    tipo_juego = models.CharField(
        max_length=25,
        choices=TIPO_JUEGO_CHOICES,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nombre


class Autores(models.Model):
    juego_serio = models.ForeignKey(JuegosSerios, on_delete=models.CASCADE, null=True)
    nombre_completo = models.CharField(max_length=100, blank=True, null=True, default='')

    def __str__(self):
        return self.nombre_completo


class Objetivos(models.Model):
    juego_serio = models.OneToOneField(JuegosSerios, on_delete=models.CASCADE)

    NO_CUBRE = 0
    PARCIALMENTE_CUBRE = 0.5
    TOTALMENTE_CUBRE = 1
    COBERTURA_CHOICES = [
        (NO_CUBRE, 'No lo cubre'),
        (PARCIALMENTE_CUBRE, 'Parcialmente lo cubre'),
        (TOTALMENTE_CUBRE, 'Totalmente lo cubre'),
    ]

    objetivo_1 = models.FloatField(
        verbose_name='entender los conceptos básicos de Kanban',
        choices=COBERTURA_CHOICES,
        default=NO_CUBRE,
    )
    objetivo_2 = models.FloatField(
        verbose_name='entender como funciona un sistema Kanban',
        choices=COBERTURA_CHOICES,
        default=NO_CUBRE,
    )
    objetivo_3 = models.FloatField(
        verbose_name='aprender los 3 principios de Change Management',
        choices=COBERTURA_CHOICES,
        default=NO_CUBRE,
    )
    objetivo_4 = models.FloatField(
        verbose_name='aprender los principios y practicas fundamentales de Kanban',
        choices=COBERTURA_CHOICES,
        default=NO_CUBRE,
    )
    objetivo_5 = models.FloatField(
        verbose_name='experimentar los beneficios de limitar el trabajo en proceso para mejorar el flujo de trabajo',
        choices=COBERTURA_CHOICES,
        default=NO_CUBRE,
    )
    objetivo_6 = models.FloatField(
        verbose_name='entender como implementar reuniones Kanban en torno al trabajo',
        choices=COBERTURA_CHOICES,
        default=NO_CUBRE,
    )
    objetivo_7 = models.FloatField(
        verbose_name='entender las métricas principales de Kanban',
        choices=COBERTURA_CHOICES,
        default=NO_CUBRE,
    )


class Jugadores(models.Model):
    juego_serio = models.OneToOneField(JuegosSerios, on_delete=models.CASCADE)
    min = models.IntegerField(blank=True, null=True, default=2)
    max = models.IntegerField(blank=True, null=True)


class Practicas(models.Model):
    juego_serio = models.OneToOneField(JuegosSerios, on_delete=models.CASCADE)
    practica_1 = models.TextField(
        verbose_name='visualizar el flujo de trabajo',
        blank=True,
    )
    practica_2 = models.TextField(
        verbose_name='limitar el trabajo en progreso (WIP)',
        blank=True,
    )
    practica_3 = models.TextField(
        verbose_name='gestionar el flujo',
        blank=True,
    )
    practica_4 = models.TextField(
        verbose_name='hacer explícitas las políticas del proceso',
        blank=True,
    )
    practica_5 = models.TextField(
        verbose_name='implementar ciclos de retroalimentación',
        blank=True,
    )
    practica_6 = models.TextField(
        verbose_name='mejorar colaborativamente',
        blank=True,
    )


class Principios(models.Model):
    juego_serio = models.OneToOneField(JuegosSerios, on_delete=models.CASCADE)
    principio_1 = models.TextField(
        verbose_name='empezar de donde estamos',
        blank=True,
    )
    principio_2 = models.TextField(
        verbose_name='acordar perseguir un cambio evolutivo incremental',
        blank=True,
    )
    principio_3 = models.TextField(
        verbose_name='respetar el proceso actual, roles, responsabilidades y títulos',
        blank=True,
    )
    principio_4 = models.TextField(
        verbose_name='fomentar actos de liderazgo en todos los niveles',
        blank=True,
    )


class Metricas(models.Model):
    juego_serio = models.OneToOneField(JuegosSerios, on_delete=models.CASCADE)
    metrica_1 = models.TextField(
        verbose_name='throughput',
        blank=True,
    )
    metrica_2 = models.TextField(
        verbose_name='tiempo de entrega',
        blank=True,
    )
    metrica_3 = models.TextField(
        verbose_name='trabajo en progreso (WIP)',
        blank=True,
    )


class Sugerencias(models.Model):
    sugerencia = models.TextField(null=False)

    SIN_EXPERIENCIA = 'Sin experiencia en Kanban'
    POCA_EXPERIENCIA = 'Poca experiencia en Kanban'
    EXPERIENCIA_CHOICES = [
        (SIN_EXPERIENCIA, 'Sin experiencia en Kanban'),
        (POCA_EXPERIENCIA, 'Poca experiencia en Kanban'),
    ]

    experiencia = models.CharField(max_length=30, choices=EXPERIENCIA_CHOICES)

    EMPRENDEDORES = 'Emprendedores'
    MIEMBROS = 'Miembros de empresas u organizaciones'
    PROFESIONISTAS = 'Profesionistas de dominios especificos'
    MAESTROS = 'Maestros'
    ESTUDIANTES = 'Estudiantes'
    PERFILES_CHOICES = [
        (EMPRENDEDORES, 'Emprendedores'),
        (MIEMBROS, 'Miembros de empresas u organizaciones'),
        (PROFESIONISTAS, 'Profesionistas de dominios especificos'),
        (MAESTROS, 'Maestros'),
        (ESTUDIANTES, 'Estudiantes'),
    ]

    perfil = models.CharField(max_length=40, choices=PERFILES_CHOICES)

    NO_APLICA = 0
    NO_TAN_IMPORTANTE = 1
    IMPORTANTE = 2
    MUY_IMPORTANTE = 3
    IMPORTANCIA_CHOICES = [
        (NO_APLICA, 'No aplica'),
        (NO_TAN_IMPORTANTE, 'No tan importante'),
        (IMPORTANTE, 'Importante'),
        (MUY_IMPORTANTE, 'Muy importante'),
    ]

    importancia = models.IntegerField(choices=IMPORTANCIA_CHOICES)

    OBJETIVOS_APRENDIZAJE = 'Objetivos de aprendizaje'
    JUEGOS_SERIOS = 'Juegos serios'
    CONCEPTOS_BASICOS = 'Conceptos básicos'
    OTRAS = 'Otras sugerencias complementarias'
    CATEGORIA_CHOICES = [
        (OBJETIVOS_APRENDIZAJE, 'Objetivos de aprendizaje'),
        (JUEGOS_SERIOS, 'Juegos serios'),
        (CONCEPTOS_BASICOS, 'Conceptos básicos'),
        (OTRAS, 'Otras sugerencias complementarias'),
    ]

    categoria = models.CharField(max_length=40, choices=CATEGORIA_CHOICES)

    def __str__(self):
        return self.sugerencia