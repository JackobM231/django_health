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
  user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="blood_preasure")
  systolic_bp = models.IntegerField(blank=False, null=False)
  diastolic_bp = models.IntegerField(blank=False, null=False)
  category = models.PositiveSmallIntegerField(default=BPCategory.NORMAL)
  note = models.TextField(max_length=500, blank=True, null=True)
  
  def save(self, *args, **kwargs):
    '''Assigns to the appropriate category of blood pressure.'''
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


class GCategory(models.IntegerChoices):
  '''GlucoseCategory'''
  LOW = 1, 'low'
  NORMAL = 2, 'normal'
  PREDIABETES = 3, 'prediabetes'
  DIABETES = 4, 'diabetes'

class Glucose(Timestamp):
  user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="glucose")
  glucose_blood = models.FloatField(blank=True, null=True)
  glucose_oral = models.FloatField(blank=True, null=True)
  category = models.PositiveSmallIntegerField(default=GCategory.NORMAL)
  note = models.TextField(max_length=500, blank=True, null=True)
  
  def save(self, *args, **kwargs):
    '''Assigns to the appropriate category of glucose.'''
    if self.glucose_blood and self.glucose_blood < 35:
      # Change 1 mmol/l = 18mg/dl
      self.glucose_blood = round(self.glucose_blood * 18)
    if self.glucose_oral and self.glucose_oral < 35:
      # Change 1 mmol/l = 18mg/dl
      self.glucose_oral = round(self.glucose_oral * 18)
    blood = self.glucose_blood
    oral = self.glucose_oral
    if blood and oral:
      # Blood and oral test
      blood_res = glucose_blood(blood)
      oral_res = glucose_oral(oral)
      self.category = max(blood_res, oral_res)
    elif not oral:
      # Blood test only
      self.category = glucose_blood(blood)
    elif not blood:
      # Oral test only
      self.category = glucose_oral(oral)
    super().save(*args, **kwargs)
  
def glucose_blood(blood):
  '''Category assignment depending of Fasting blood sugar test.'''
  # if blood > 35:
  if blood < 70:
    return GCategory.LOW
  elif blood < 100:
    return GCategory.NORMAL
  elif blood <= 125:
    return GCategory.PREDIABETES
  else:
    return GCategory.DIABETES
  # else:
  #   if blood < 3.9:
  #     return GCategory.LOW
  #   elif blood < 5.6:
  #     return GCategory.NORMAL
  #   elif blood <= 6.9:
  #     return GCategory.PREDIABETES
  #   else:
  #     return GCategory.DIABETES

def glucose_oral(oral):
  '''Category assignment depending of Oral glucose tolerance test.'''
  # if oral > 35:
  if oral < 60:
    return GCategory.LOW
  elif oral < 140:
    return GCategory.NORMAL
  elif oral <= 199:
    return GCategory.PREDIABETES
  else:
    return GCategory.DIABETES
  # else:
  #   if oral < 7.8:
  #     return GCategory.NORMAL
  #   elif oral <= 11:
  #     return GCategory.PREDIABETES
  #   else:
  #     return GCategory.DIABETES