# Generated by Django 3.1 on 2020-09-21 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20200921_0317'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='Feeds',
        ),
    ]
