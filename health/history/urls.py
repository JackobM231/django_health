from django.urls import path
from .views import BloodPreasureHistory

app_name = 'history'
urlpatterns = [
  path('blood_preasure', BloodPreasureHistory, name='blood_preasure'),
  # path('pulse', PulseHistory, name='blood_preasure'),
  # path('glucose', GlucoseHistory, name='blood_preasure'),
]