# Generated by Django 4.2 on 2023-05-09 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_product_expiry_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('counts', models.CharField(choices=[('10', '10'), ('15', '15'), ('1', '1')], max_length=20, null=True)),
                ('manufacturer', models.CharField(max_length=100, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('batch_number', models.CharField(max_length=100, null=True)),
                ('expiry_date', models.DateField(blank=True)),
                ('mrp_per_unit', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]