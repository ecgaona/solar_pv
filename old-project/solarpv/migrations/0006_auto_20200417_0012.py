# Generated by Django 3.0.4 on 2020-04-17 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solarpv', '0005_auto_20200417_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
    ]
