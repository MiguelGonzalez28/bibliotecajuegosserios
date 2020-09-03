from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, error_messages={'required': 'Este campo es obligatorio'})
    email = forms.EmailField(error_messages={'required': 'Este campo es obligatorio'})
    mensaje = forms.CharField(widget=forms.Textarea, error_messages={'required': 'Este campo es obligatorio', 'invalid': 'Introduzca una dirección válida'})


class SugerenciasForm(forms.Form):
    OBJETIVOS_APRENDIZAJE = 'Objetivos de aprendizaje'
    JUEGOS_SERIOS = 'Juegos serios'
    OTRAS = 'Otras sugerencias complementarias'
    CATEGORIA_CHOICES = [
        ('', ''),
        (OBJETIVOS_APRENDIZAJE, 'Objetivos de aprendizaje'),
        (JUEGOS_SERIOS, 'Juegos serios'),
        (OTRAS, 'Otras sugerencias complementarias'),
    ]

    categoria = forms.ChoiceField(choices=CATEGORIA_CHOICES, label='Sugerencias sobre:',
                                  help_text='Este campo es requerido',
                                  error_messages={'required': 'Este campo es obligatorio'})

    SIN_EXPERIENCIA = 'Sin experiencia en Kanban'
    POCA_EXPERIENCIA = 'Poca experiencia en Kanban'
    EXPERIENCIA_CHOICES = [
        ('', ''),
        (SIN_EXPERIENCIA, 'Sin experiencia en Kanban'),
        (POCA_EXPERIENCIA, 'Poca experiencia en Kanban'),
    ]

    experiencia = forms.ChoiceField(choices=EXPERIENCIA_CHOICES,
                                    required=False, help_text='Experiencia de los participantes')

    EMPRENDEDORES = 'Emprendedores'
    MIEMBROS = 'Miembros de empresas u organizaciones'
    PROFESIONISTAS = 'Profesionistas de dominios especificos'
    MAESTROS = 'Maestros'
    ESTUDIANTES = 'Estudiantes'
    PERFILES_CHOICES = [
        ('', ''),
        (EMPRENDEDORES, 'Emprendedores'),
        (MIEMBROS, 'Miembros de empresas u organizaciones'),
        (PROFESIONISTAS, 'Profesionistas de dominios específicos'),
        (MAESTROS, 'Maestros'),
        (ESTUDIANTES, 'Estudiantes'),
    ]

    perfil = forms.ChoiceField(choices=PERFILES_CHOICES, required=False, help_text='Perfil de los participantes')