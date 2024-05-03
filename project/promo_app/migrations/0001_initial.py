# Generated by Django 5.0.4 on 2024-05-01 22:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('annee', models.CharField(default='2023-2024', max_length=10)),
                ('niveau', models.CharField(default='1cp', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Chapitre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_deposer', models.DateTimeField(auto_now_add=True)),
                ('nom', models.CharField(max_length=20)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promo_app.module')),
            ],
        ),
        migrations.CreateModel(
            name='Mooc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('nom', models.CharField(blank=True, max_length=100)),
                ('durée', models.CharField(max_length=20)),
                ('chapitre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promo_app.chapitre')),
            ],
        ),
    ]
