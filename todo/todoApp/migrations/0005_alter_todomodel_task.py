# Generated by Django 4.1.5 on 2023-01-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0004_alter_todomodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='task',
            field=models.CharField(max_length=150),
        ),
    ]
