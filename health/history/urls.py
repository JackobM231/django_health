from django.urls import path
from .views import BloodPreasureHistory, BloodPreasureDetail, PulseHistory, PulseDetail, GlucoseHistory, GlucoseDetail

app_name = 'history'
urlpatterns = [
  path('blood_preasure', BloodPreasureHistory, name='blood_preasure_history'),
  path('blood_preasure/details/<int:measurement_id>', BloodPreasureDetail, name='blood_preasure_details'),
  path('pulse', PulseHistory, name='pulse_history'),
  path('pulse/details/<int:measurement_id>', PulseDetail, name='pulse_details'),
  path('glucose', GlucoseHistory, name='glucose_history'),
  path('glucose/details/<int:measurement_id>', GlucoseDetail, name='glucose_details'),
]