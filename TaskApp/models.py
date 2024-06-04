from django.db import models
from categoryApp.models import CategoryModel
from datetime import date
class TaskModel(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(default='')
    is_complete = models.BooleanField(default=False)
    date = models.DateField(default=date.today)
    category = models.ManyToManyField(CategoryModel)

    def __str__(self):
        return self.title

