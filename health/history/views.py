from datetime import datetime
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse

from measurements.models import BloodPreasure, BPCategory, Pulse, Glucose
from measurements.forms import BloodPreasureFormEdit

# Create your views here.

@login_required
def BloodPreasureHistory(request):
  user = request.user
  history = BloodPreasure.objects.filter(user=user)
  
  # Number of elements per page
  if request.method == 'POST':
    elem_on_page = int(request.POST.get('selected').strip('-'))
  # Elements after selecting
  if request.method == 'GET':
    try:
      elem_on_page = int(request.GET.get('elem'))
    except:
      elem_on_page = 10
      # Default number of elements on page
  
  # Pagination
  paginator = Paginator(history, elem_on_page)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  
  return render(request,
                'history/blood.html',
                {'page_obj': page_obj,
                  'elem_on_page': elem_on_page,
                  'category': BPCategory}
                )
  
  
def BloodPreasureDetail(request, measurement_id):
  measurement = get_object_or_404(BloodPreasure, id=measurement_id)
  if request.user == measurement.user:
    if request.method == 'POST':
      if request.POST.get('delete') == 'Delete':
        measurement.delete()
        return HttpResponseRedirect(reverse('history:blood_preasure'))
      else:
        form = BloodPreasureFormEdit(request.POST, instance=measurement)
        # Instance - we are saving current measurement object not new object
        if form.is_valid():
          instance = form.save(commit=False)
          instance.user = request.user
          instance.save()
          return render(request, 'history/details.html',
                        {'form': form,
                         'm_category': measurement.category,
                         'category': BPCategory,
                         'info': 'Saved'})
    else:
      form = BloodPreasureFormEdit(instance=measurement)
      return render(request, 'history/details.html',
                    {'form': form,
                    'm_category': measurement.category,
                    'category': BPCategory})
  else:
    return HttpResponseRedirect(reverse_lazy('login'))