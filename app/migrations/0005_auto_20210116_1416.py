# Generated by Django 3.1.2 on 2021-01-16 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210116_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='likes', to='app.User'),
        ),
    ]