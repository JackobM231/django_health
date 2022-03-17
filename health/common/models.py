from email.policy import default
from django.db import models
from django.utils import timezone
# from datetime import datetime

# Create your models here.

class Timestamp(models.Model):
  class Meta:
    abstract = True
    # Class for inheritance only
    ordering = ['created']
    
  # created = models.DateTimeField(auto_now_add=True)
  created = models.DateTimeField(default=timezone.now, blank=True)
  modified = models.DateTimeField(auto_now=True)
  