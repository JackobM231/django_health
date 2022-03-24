from django.urls import path
from measurements.views import blood_measure, glucose_measure

app_name = 'measurements'
urlpatterns = [
  path('blood/', blood_measure, name='blood_measure'),
  path('glucose/', glucose_measure, name='glucose_measure'),
]