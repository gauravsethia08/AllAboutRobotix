# Generated by Django 3.1.3 on 2020-11-24 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201119_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='make_public',
            field=models.BooleanField(default=True),
        ),
    ]
