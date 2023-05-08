# Generated by Django 4.2.1 on 2023-05-04 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('synopsis', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
