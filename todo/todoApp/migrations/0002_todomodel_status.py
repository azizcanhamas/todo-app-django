# Generated by Django 4.1.5 on 2023-01-16 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='status',
            field=models.TextField(default='Devam ediyor.'),
            preserve_default=False,
        ),
    ]
