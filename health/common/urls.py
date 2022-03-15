from django.urls import path
from .views import home

app_name = 'common'
urlpatterns = [
  path('', home, name='home'),
]