from django.db import models

# Create your models here.
class ProjectEntry(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    dates = models.DateField()