# Generated by Django 3.1 on 2020-09-21 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20200921_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeds',
            name='news_category',
            field=models.TextField(default='Без категории', null=True),
        ),
        migrations.AlterField(
            model_name='shopitem',
            name='category_name',
            field=models.TextField(default='Без категории'),
        ),
    ]
