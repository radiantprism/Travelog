# Generated by Django 3.0.5 on 2020-05-20 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsite', '0002_attraction_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]