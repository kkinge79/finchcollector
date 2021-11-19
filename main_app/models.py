from django.db import models

# Create your models here.
from django.db import models

class Finch(models.Model):
  name = models.CharField(max_length=100)
  sex = models.CharField(max_length=20)
  description = models.TextField(max_length=250)
  color = models.TextField(max_length=30)