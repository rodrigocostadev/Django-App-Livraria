# Generated by Django 5.1.5 on 2025-02-13 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0014_userprofile_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cpf',
            field=models.IntegerField(default=0),
        ),
    ]
