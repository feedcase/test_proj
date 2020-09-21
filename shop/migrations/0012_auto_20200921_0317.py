# Generated by Django 3.1 on 2020-09-21 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200921_0242'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_body',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='news_image',
            field=models.ImageField(null=True, upload_to='F:\\workspace\\python\\test_proj\\media'),
        ),
        migrations.AddField(
            model_name='news',
            name='news_post_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
