# Generated by Django 4.1.5 on 2023-01-16 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoModel',
            fields=[
                ('id', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('task', models.TextField(max_length=100)),
            ],
        ),
    ]
