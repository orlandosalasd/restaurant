# Generated by Django 3.2.7 on 2021-09-10 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_alter_profile_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': [('administrator_access', 'Administrator access'), ('customer_access', 'Customer access')]},
        ),
    ]