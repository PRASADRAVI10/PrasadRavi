# Generated by Django 3.2.16 on 2023-01-11 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='image', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
