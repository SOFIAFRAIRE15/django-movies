# Generated by Django 4.2.1 on 2023-05-08 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
