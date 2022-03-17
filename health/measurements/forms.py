from django import forms
# from datetime import datetime
from django.utils import timezone

from .models import BloodPreasure, Pulse, Glucose

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder, Field, Fieldset, Row, Column

class BloodPreasuerForm(forms.ModelForm):
  class Meta:
    model = BloodPreasure
    fields = ['systolic_bp', 'diastolic_bp', 'created', 'note']
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.form_action = ''
    self.helper.layout = Layout(
      Field(
        'systolic_bp', css_class='mb-3'
      ),
      Field(
        'diastolic_bp', css_class='mb-3'
      ),
      Field(
        'created', placeholder=timezone.now(), css_class='mb-3'
      ),
      Field(
        'note', placeholder=' Some info for yourself in the future...', css_class='w-100'
      ),
      ButtonHolder(
        Submit('submit', 'Save', css_class='btn btn-primary'),
        css_class='d-flex justify-content-center mt-2'
      )
    )
    # self.helper.layout = Layout(
    #   Row(
    #     Column('systolic_bp', css_class='form-group col-md-6'),
    #     Column('diastolic_bp', css_class='form-group col-md-6'),
    #     css_class='form-row'
    #   ),
    #   Field(
    #     'note', placeholder=' Some info for yourself in the future...'
    #   ),
    #   ButtonHolder(
    #     Submit('submit', 'Save', css_class='btn btn-primary'),
    #     css_class='d-flex justify-content-center mt-2'
    #   )
    # )