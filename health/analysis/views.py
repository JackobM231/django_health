from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Avg, Max, Min

from measurements.models import BloodPreasure

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

  # diastolic = { 'max': data.aggregate(Max('diastolic_bp')),
  #               'min': data.aggregate(Min('diastolic_bp')),
  #               'avg': data.aggregate(Avg('diastolic_bp'))
  #               }
  
  return render(request, 'analysis/blood.html',
                {'data': data,
                  'systolic': [systolic_max, systolic_min, systolic_avg],
                  'diastolic': [diastolic_max, diastolic_min, diastolic_avg]
                })