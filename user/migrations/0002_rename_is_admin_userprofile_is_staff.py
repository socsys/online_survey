# Generated by Django 5.0.4 on 2024-04-29 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]
