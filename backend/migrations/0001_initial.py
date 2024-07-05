# Generated by Django 5.0.6 on 2024-07-03 11:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catégorie',
            fields=[
                ('idCategorie', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='pharmacies/photos/')),
                ('nom', models.CharField(blank=True, null=True)),
                ('adresse', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('password', models.CharField(max_length=255)),
                ('repassword', models.CharField(max_length=255)),
                ('proprietaire', models.CharField(blank=True, max_length=255, null=True)),
                ('numero_ordre', models.CharField(blank=True, max_length=100, null=True)),
                ('licence_exploitation', models.FileField(blank=True, null=True, upload_to='pharmacie/autorisation/')),
                ('attestation_professionnelle', models.FileField(blank=True, null=True, upload_to='pharmacie/attestation/')),
                ('is_admin', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pharmacie', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Produits',
            fields=[
                ('idProduit', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='Produits')),
                ('Medicament', models.CharField(max_length=255)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField()),
                ('auteur', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.pharmacie')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.catégorie')),
            ],
        ),
    ]