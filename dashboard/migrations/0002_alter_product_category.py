# Generated by Django 4.2 on 2023-04-30 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('stationary', 'stationary'), ('Electronics', 'Electronics'), ('Food', 'Food')], max_length=20, null=True),
        ),
    ]
