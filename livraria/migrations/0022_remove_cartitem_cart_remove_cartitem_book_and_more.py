# Generated by Django 5.1.5 on 2025-02-24 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0021_alter_userprofile_cpf_cart_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='book',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
