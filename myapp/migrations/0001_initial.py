# Generated by Django 2.0.5 on 2018-12-01 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor_profile', '0001_initial'),
        ('rmp', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rmplist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rmp_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmp.rmpContact')),
            ],
        ),
    ]
