# Generated by Django 5.0.6 on 2024-07-31 22:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_remove_vente_medicament_vente_produit'),
    ]

    operations = [
        migrations.AddField(
            model_name='vente',
            name='date_commande',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
