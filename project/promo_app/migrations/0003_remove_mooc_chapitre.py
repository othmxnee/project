# Generated by Django 5.0.4 on 2024-05-01 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promo_app', '0002_rename_durée_mooc_duree'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mooc',
            name='chapitre',
        ),
    ]
