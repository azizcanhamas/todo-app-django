# Generated by Django 4.1.5 on 2023-01-16 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0003_alter_todomodel_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]