# Generated by Django 5.0 on 2023-12-22 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('name',), 'verbose_name': 'course', 'verbose_name_plural': 'courses'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ('name',), 'verbose_name': 'dept', 'verbose_name_plural': 'department'},
        ),
    ]
