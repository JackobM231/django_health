from django.urls import path
from measurements.views import blood_measure, pulse_measure, glucose_measure

app_name = 'measurements'
urlpatterns = [
  path('blood/', blood_measure, name='blood_measure'),
  path('pulse/', pulse_measure, name='pulse_measure'),
  path('glucose/', glucose_measure, name='glucose_measure'),
]