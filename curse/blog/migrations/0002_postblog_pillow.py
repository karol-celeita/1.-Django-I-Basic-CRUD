# Generated by Django 2.2 on 2020-04-06 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postblog',
            name='pillow',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
