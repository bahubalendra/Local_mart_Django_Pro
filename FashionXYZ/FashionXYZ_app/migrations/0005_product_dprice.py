# Generated by Django 3.0.7 on 2020-07-07 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FashionXYZ_app', '0004_auto_20200707_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dprice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
