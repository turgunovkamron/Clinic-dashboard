# Generated by Django 4.2.3 on 2023-08-09 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_price_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='familya',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='familya'),
        ),
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='docs', verbose_name='rasm'),
        ),
        migrations.AlterField(
            model_name='user',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='SHifokor haqida qisqacha'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='ismi'),
        ),
    ]
