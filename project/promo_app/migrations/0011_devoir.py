# Generated by Django 5.0.4 on 2024-05-02 10:28

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo_app', '0010_cours_chapitre_fiche_chapitre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devoir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField(auto_created=True)),
                ('nom', models.CharField(max_length=50)),
                ('date_fin', models.DateField(blank=True, null=True)),
                ('file', models.FileField(upload_to='uploads/', validators=[django.core.validators.FileExtensionValidator(['ppt', 'pdf'])])),
                ('Chapitre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promo_app.chapitre')),
            ],
        ),
    ]