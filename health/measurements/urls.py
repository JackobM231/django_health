from django.urls import path
from measurements.views import blood_measure

app_name = 'measurements'
urlpatterns = [
  path('blood/', blood_measure, name='blood_measure'),
]