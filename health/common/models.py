from django.db import models

# Create your models here.

class Timestamp(models.Model):
  class Meta:
    abstract = True
    # Class for inheritance only
    
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  