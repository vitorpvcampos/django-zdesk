# Generated by Django 3.0.3 on 2020-02-12 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0005_ticketupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='order',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Código do pedido'),
        ),
    ]
