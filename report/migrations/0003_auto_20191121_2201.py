# Generated by Django 2.2.7 on 2019-11-21 14:01

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20191121_2051'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='report',
            managers=[
                ('object_', django.db.models.manager.Manager()),
            ],
        ),
    ]
