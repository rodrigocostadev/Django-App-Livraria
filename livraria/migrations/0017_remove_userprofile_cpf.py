# Generated by Django 5.1.5 on 2025-02-13 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0016_alter_userprofile_cpf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='cpf',
        ),
    ]
