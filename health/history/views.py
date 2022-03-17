from datetime import datetime
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from measurements.models import BloodPreasure, BPCategory, Pulse, Glucose

# Create your views here.

def BloodPreasureHistory(request):
  user = request.user
  if user.is_authenticated:
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
  else:
    return HttpResponseRedirect(reverse_lazy('login'))