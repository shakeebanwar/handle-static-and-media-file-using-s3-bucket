# Generated by Django 3.2.4 on 2021-06-25 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='super_adminaccount',
            old_name='Fname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='super_adminaccount',
            old_name='Profile',
            new_name='qr_code',
        ),
    ]
