from django.urls import path
from analysis.views import blood_analysis, pulse_analysis, glucose_analysis

app_name = 'analysis'
urlpatterns = [
  path('blood/', blood_analysis, name='blood_preasure_analysis'),
  path('pulse/', pulse_analysis, name='pulse_analysis'),
  path('glucose/', glucose_analysis, name='glucose_analysis'),
]