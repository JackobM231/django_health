from django.db import models
from common.models import Timestamp

# Create your models here.

class BloodPreasure(Timestamp):
  user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="blood_preasure")
  systolic_bp = models.IntegerField(blank=False, null=False)
  diastolic_bp = models.IntegerField(blank=False, null=False)
  note = models.TextField(max_length=500, blank=True, null=True)
  
  
class Pulse(Timestamp):
  user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="pulse")
  pulse = models.IntegerField(blank=False, null=False)
  note = models.TextField(max_length=500, blank=True, null=True)
  

class Glucose(Timestamp):
  user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="glucose")
  glucose = models.IntegerField(blank=False, null=False)
  note = models.TextField(max_length=500, blank=True, null=True)