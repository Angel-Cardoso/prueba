# Generated by Django 2.1 on 2018-11-05 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reunione_Cliente',
            new_name='Reunion_Cliente',
        ),
        migrations.RenameModel(
            old_name='Reunione_Personal',
            new_name='Reunion_Personal',
        ),
    ]