import factory
from factory import fuzzy
from faker import Factory
from datetime import datetime

from django.contrib.auth.models import User

faker = Factory.create()

def get_user():
  users = User.objects.all()
  return users.values_list('id', flat=True)
  

class BPMFactory(factory.django.DjangoModelFactory):
  '''Creating random Blood Preasure Measurements for choosed random user.'''
  # users = get_user()
  
  class Meta:
    model = 'measurements.BloodPreasure'
  
  user = factory.fuzzy.FuzzyChoice(User.objects.all())
  systolic_bp = factory.LazyAttribute(lambda x: faker.random.randint(60, 190))
  diastolic_bp = factory.LazyAttribute(lambda x: faker.random.randint(50, 125))
  note = factory.LazyAttribute(lambda x: faker.text(100))
  created = factory.LazyAttribute(lambda x: faker.date_time_between(datetime(2021,8,1,11,42,52)))
  
  # Fast shell commend
  #  from measurements.factories import BPMFactory as F
  #  from django.contrib.auth.models import User
  #  admin = User.objects.get(pk=1)
  #  F.create_batch(user=admin, size=25)
  
  # user = factory.fuzzy.FuzzyChoice(User.objects.all())
  # systolic_bp = factory.fuzzy.FuzzyInteger(60, 190)
  # diastolic_bp = factory.fuzzy.FuzzyInteger(50, 125)
  # note = factory.fuzzy.FuzzyText(100)
  # created = factory.fuzzy.FuzzyNaiveDateTime(datetime(2021, 1, 1))