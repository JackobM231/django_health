from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Avg, Max, Min

from measurements.models import BloodPreasure, Glucose

# Create your views here.
@login_required
def blood_analysis(request):
  data = BloodPreasure.objects.filter(user_id=request.user.id)
  systolic_max = data.aggregate(Max('systolic_bp'))['systolic_bp__max'],
  systolic_min = data.aggregate(Min('systolic_bp'))['systolic_bp__min'],
  systolic_avg = int(data.aggregate(Avg('systolic_bp'))['systolic_bp__avg'])
  
  diastolic_max = data.aggregate(Max('diastolic_bp'))['diastolic_bp__max'],
  diastolic_min = data.aggregate(Min('diastolic_bp'))['diastolic_bp__min'],
  diastolic_avg = int(data.aggregate(Avg('diastolic_bp'))['diastolic_bp__avg'])
  
  if systolic_avg > 180 or diastolic_avg > 120:
    category = 'table-height-danger'
  elif systolic_avg >= 140 or diastolic_avg >= 90:
    category = 'table-danger'
  elif systolic_avg >= 130 or diastolic_avg >= 80:
    category = 'table-height-warning'
  elif systolic_avg < 90 and diastolic_avg < 60:
    category = 'table-info'
  elif systolic_avg <120 and diastolic_avg < 80:
    category = 'table-success'
  else:
    category = 'table-warning'
  
  return render(request, 'analysis/blood.html',
                {'data': data,
                  'systolic': [systolic_max, systolic_min, systolic_avg],
                  'diastolic': [diastolic_max, diastolic_min, diastolic_avg],
                  'category': category
                })
  
  
@login_required
def glucose_analysis(request):
  data = Glucose.objects.filter(user_id=request.user.id)
  blood_max = data.aggregate(Max('glucose_blood'))['glucose_blood__max'],
  blood_min = data.aggregate(Min('glucose_blood'))['glucose_blood__min'],
  blood_avg = int(data.aggregate(Avg('glucose_blood'))['glucose_blood__avg'])
  
  oral_max = data.aggregate(Max('glucose_oral'))['glucose_oral__max'],
  oral_min = data.aggregate(Min('glucose_oral'))['glucose_oral__min'],
  oral_avg = int(data.aggregate(Avg('glucose_oral'))['glucose_oral__avg'])
  
  if blood_avg < 70 or oral_avg < 60:
    category = 'table-warning'
  elif blood_avg < 100 and oral_avg < 140:
    category = 'table-success'
  elif blood_avg <= 125 and oral_avg <= 199:
    category = 'table-height-warning'
  else:
    category = 'table-height-danger'
  
  return render(request, 'analysis/glucose.html',
                {'data': data,
                  'blood_test': [blood_max, blood_min, blood_avg],
                  'oral_test': [oral_max, oral_min, oral_avg],
                  'category': category
                })