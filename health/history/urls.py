from django.urls import path
from .views import BloodPreasureHistory, BloodPreasureDetail

app_name = 'history'
urlpatterns = [
  path('blood_preasure', BloodPreasureHistory, name='blood_preasure'),
  path('blood_preasure/details/<int:measurement_id>', BloodPreasureDetail, name='blood_preasure_details'),
  # path('pulse', PulseHistory, name='blood_preasure'),
  # path('glucose', GlucoseHistory, name='blood_preasure'),
]