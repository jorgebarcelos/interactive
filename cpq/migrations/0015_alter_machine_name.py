# Generated by Django 4.2.5 on 2023-10-17 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpq', '0014_machine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
