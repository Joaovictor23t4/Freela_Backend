# Generated by Django 5.1.1 on 2024-10-01 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_rename_confirmation_token_user_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverification',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
