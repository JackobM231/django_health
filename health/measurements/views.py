from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import BloodPreasureForm, PulseForm, GlucoseForm

# Create your views here.
def blood_measure(request):
  if request.method == 'POST' and request.user.is_authenticated:
    form = BloodPreasureForm(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.user = request.user
      instance.save()
      return HttpResponseRedirect(reverse('measurements:blood_measure'))
  else:
    form = BloodPreasureForm()
  return render(request, 'measurements/blood.html', {'form': form})


def pulse_measure(request):
  if request.method == 'POST' and request.user.is_authenticated:
    form = PulseForm(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.user = request.user
      instance.save()
      return HttpResponseRedirect(reverse('measurements:pulse_measure'))
  else:
    form = PulseForm()
  return render(request, 'measurements/pulse.html', {'form': form})


def glucose_measure(request):
  if request.method == 'POST' and request.user.is_authenticated:
    form = GlucoseForm(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.user = request.user
      instance.save()
      return HttpResponseRedirect(reverse('measurements:glucose_measure'))
  else:
    form = GlucoseForm()
  return render(request, 'measurements/glucose.html', {'form': form})