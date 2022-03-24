from django.urls import path
from .views import BloodPreasureHistory, BloodPreasureDetail, GlucoseHistory, GlucoseDetail

app_name = 'history'
urlpatterns = [
  path('blood_preasure', BloodPreasureHistory, name='blood_preasure_history'),
  path('blood_preasure/details/<int:measurement_id>', BloodPreasureDetail, name='blood_preasure_details'),
  path('glucose', GlucoseHistory, name='glucose_history'),
  path('glucose/details/<int:measurement_id>', GlucoseDetail, name='glucose_details'),
  # path('pulse', PulseHistory, name='blood_preasure'),
  # path('glucose', GlucoseHistory, name='blood_preasure'),
]