# Generated by Django 2.2.2 on 2019-06-07 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190607_2147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ['id'], 'verbose_name': 'OrderItem', 'verbose_name_plural': 'OrderItems'},
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='count',
            field=models.PositiveIntegerField(verbose_name='count'),
        ),
    ]
