# Generated by Django 4.2 on 2023-05-09 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='batch_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='counts',
            field=models.CharField(choices=[('10', '10'), ('15', '15'), ('1', '1')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='mrp_per_unit',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='purchase_rate',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='rack',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='suppliers_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
