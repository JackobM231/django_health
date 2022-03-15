from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import RegisterForm
from django.contrib.auth.models import User, Group

# Create your views here.
def register(response):
  if response.method == 'POST':
    form = RegisterForm(response.POST)
    if form.is_valid():
      form.save()
      # Add new user to 'default user' group
      username = form.cleaned_data['username']
      user = User.objects.get(username=username)
      group = Group.objects.get(name='default user')
      group.user_set.add(user)
    return HttpResponseRedirect(reverse_lazy('login'))     
  else:
    form = RegisterForm()
  return render(response, 'accounts/register.html', {'form': form})


def login(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(request, username=username, password=password)
  if user is not None:
    login(request, user)
    # Redirection to success page
  else:
    pass
  # Redirection to fail page
  