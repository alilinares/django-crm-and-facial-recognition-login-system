# Generated by Django 3.2.9 on 2023-04-13 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
