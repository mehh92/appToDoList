# Generated by Django 4.2.13 on 2024-06-13 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_todolist', '0002_remove_utilisateur_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='statut',
            field=models.CharField(choices=[('en_cours', 'En cours'), ('terminee', 'Terminée')], max_length=50),
        ),
    ]
