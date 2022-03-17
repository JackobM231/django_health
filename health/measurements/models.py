from unicodedata import category
from django.db import models
from common.models import Timestamp

# Create your models here.

class BPCategory(models.IntegerChoices):
  '''BloodPreasureCategory'''
  LOW = 1, 'low'
  NORMAL = 2, 'normal'
  ELEVATED = 3, 'elevated'
  STAGE_1 = 4, 'stage_1'
  STAGE_2 = 5, 'stage_2'
  CRISIS = 6, 'crisis'

class BloodPreasure(Timestamp):
  # def category_selector(systolic, diastolic):
  #   '''Assigns to the appropriate category of blood pressure'''
  #   diastolic = int(diastolic)
  #   systolic = int(systolic)
  #   if systolic > 180 or diastolic > 120:
  #     return BPCategory.CRISIS
  #   elif systolic >= 140 or diastolic >= 90:
  #     return BPCategory.STAGE_2
  #   elif systolic >= 130 or diastolic >= 80:
  #     return BPCategory.STAGE_1
  #   elif systolic < 90 and diastolic < 60:
  #     return BPCategory.LOW
  #   elif systolic <120 and diastolic < 80:
  #     return BPCategory.NORMAL
  #   else:
  #     return BPCategory.ELEVATED
    
  user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="blood_preasure")
  systolic_bp = models.IntegerField(blank=False, null=False)
  diastolic_bp = models.IntegerField(blank=False, null=False)
  category = models.PositiveSmallIntegerField(default=BPCategory.NORMAL)
  note = models.TextField(max_length=500, blank=True, null=True)
  
  def save(self, *args, **kwargs):
    '''Assigns to the appropriate category of blood pressure'''
    diastolic = self.diastolic_bp
    systolic = self.systolic_bp
    if systolic > 180 or diastolic > 120:
      self.category=BPCategory.CRISIS
    elif systolic >= 140 or diastolic >= 90:
      self.category=BPCategory.STAGE_2
    elif systolic >= 130 or diastolic >= 80:
      self.category=BPCategory.STAGE_1
    elif systolic < 90 and diastolic < 60:
      self.category=BPCategory.LOW
    elif systolic <120 and diastolic < 80:
      self.category=BPCategory.NORMAL
    else:
      self.category=BPCategory.ELEVATED
    super().save(*args, **kwargs)
  
  def __str__(self):
    return f"BP: {self.systolic_bp}/{self.diastolic_bp} - {self.user}"
  
  
class Pulse(Timestamp):
  user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="pulse")
  pulse = models.IntegerField(blank=False, null=False)
  note = models.TextField(max_length=500, blank=True, null=True)
  

class Glucose(Timestamp):
  user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="glucose")
  glucose = models.IntegerField(blank=False, null=False)
  note = models.TextField(max_length=500, blank=True, null=True)