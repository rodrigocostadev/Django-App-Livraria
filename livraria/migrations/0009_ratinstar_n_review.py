# Generated by Django 5.1.5 on 2025-02-12 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0008_ratinstar'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratinstar',
            name='n_review',
            field=models.IntegerField(default=0),
        ),
    ]
