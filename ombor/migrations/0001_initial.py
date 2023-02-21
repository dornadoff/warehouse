# Generated by Django 4.1.7 on 2023-02-21 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('brend', models.CharField(max_length=500)),
                ('narx', models.FloatField()),
                ('kelgan_sana', models.DateField()),
                ('miqdor', models.CharField(max_length=100)),
                ('olchov', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ombor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('tel', models.CharField(max_length=14)),
                ('ism', models.CharField(max_length=100)),
                ('manzil', models.CharField(max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('manzil', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=14)),
                ('qarz', models.FloatField()),
                ('ombor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ombor.ombor')),
            ],
        ),
    ]