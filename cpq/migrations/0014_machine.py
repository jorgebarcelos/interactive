# Generated by Django 4.2.5 on 2023-10-17 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpq', '0013_alter_material_price_alter_orderitem_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cpq.manufacturer')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cpq.material')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cpq.supplier')),
            ],
        ),
    ]
