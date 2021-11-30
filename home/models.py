from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length= 100, null=True)
    description = models.CharField(max_length= 255, null=True)
    link = models.CharField(max_length= 255, null=True)

    def __str__(self):
        return self.name