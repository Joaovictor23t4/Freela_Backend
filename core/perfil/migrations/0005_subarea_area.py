# Generated by Django 5.1.1 on 2024-09-11 13:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_area_nacionality_rename_categoriafreelancer_subarea_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subarea',
            name='Area',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='perfil.area'),
            preserve_default=False,
        ),
    ]
