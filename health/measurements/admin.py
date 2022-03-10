from django.contrib import admin
from .models import BloodPreasure, Pulse, Glucose

# Register your models here.
@admin.register(BloodPreasure)
class BloodPreasureAdmin(admin.ModelAdmin):
  pass


@admin.register(Pulse)
class PulseAdmin(admin.ModelAdmin):
  pass


@admin.register(Glucose)
class GlucoseAdmin(admin.ModelAdmin):
  pass
