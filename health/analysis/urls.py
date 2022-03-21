from django.urls import path
from analysis.views import blood_analysis

app_name = 'analysis'
urlpatterns = [
  path('blood/', blood_analysis, name='blood_analysis')
]