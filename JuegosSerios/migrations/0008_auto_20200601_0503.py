# Generated by Django 3.0.6 on 2020-06-01 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JuegosSerios', '0007_sugerencias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sugerencias',
            name='importancia',
            field=models.IntegerField(choices=[(0, 'No aplica'), (1, 'No tan importante'), (2, 'Importante'), (3, 'Muy importante')]),
        ),
    ]
