from django.db import models

# Create your models here.
class ToDoList(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    completed=models.BooleanField(default=False)
