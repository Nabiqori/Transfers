# Generated by Django 5.1.6 on 2025-02-15 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='name',
        ),
    ]
