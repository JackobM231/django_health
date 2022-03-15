from django import forms

from .models import BloodPreasure, Pulse, Glucose

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Field

class BloodPreasuerForm(forms.ModelForm):
  class Meta:
    model = BloodPreasure
    fields = ['systolic_bp', 'diastolic_bp', 'note']
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.form_action = ''
    self.helper.layout = Layout(
      Fieldset(
        'Input your blood pressure measurements',
        'systolic_bp',
        'diastolic_bp',
        Field('note', placeholder='Some info for you in the future...')
      ),
      ButtonHolder(
        Submit('submit', 'Save', css_class='btn btn-primary'),
        css_class='d-flex justify-content-center mt-2'
      )
    )