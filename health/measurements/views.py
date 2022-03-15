from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import BloodPreasuerForm

# Create your views here.
def blood_measure(request):
  if request.method == 'POST' and request.user.is_authenticated:
    form = BloodPreasuerForm(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.user = request.user
      instance.save()
      return HttpResponseRedirect(reverse('measurements:blood_measure'))
  else:
    form = BloodPreasuerForm()
  return render(request, 'measurements/blood.html', {'form': form})
