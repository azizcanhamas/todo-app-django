from django.db import models

# Create your models here.

class ToDoModel(models.Model):
    id=models.AutoField(primary_key=True)
    task=models.CharField(max_length=100)
    status=models.TextField(default='Tamamlanmadı')
