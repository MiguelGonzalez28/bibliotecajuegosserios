# Generated by Django 3.0.6 on 2020-05-25 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JuegosSerios', '0004_auto_20200518_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juegosserios',
            name='idioma',
            field=models.CharField(blank=True, choices=[('Español', 'Español'), ('Inglés', 'Ingles'), ('Francés', 'Frances'), ('Portugués', 'Portugues'), ('Otro', 'Otro')], max_length=10, null=True),
        ),
    ]
