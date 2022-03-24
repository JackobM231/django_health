from django import forms
# from datetime import datetime
from django.utils import timezone

from .models import BloodPreasure, Pulse, Glucose

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder, Field, HTML

class BloodPreasureForm(forms.ModelForm):
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
        'systolic_bp',
      ),
      Field(
        'diastolic_bp',
      ),
      Field(
        'created', placeholder=timezone.now(),
      ),
      Field(
        'note', rows=5, placeholder=' Some info for yourself in the future...', css_class='w-100'
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
    
class BloodPreasureFormEdit(BloodPreasureForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
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
          'note', rows=5, placeholder=' Some info for yourself in the future...', css_class='w-100'
        ),
        ButtonHolder(
          Submit('submit', 'Save', css_class='btn btn-succes'),
          Submit('delete', 'Delete', css_class='btn btn-danger mx-3'),
          HTML('''{% if info %}<p class="align-self-center mb-0 jump-into">{{ info }}</p>{% endif %}'''),
          css_class='d-flex mt-2 mb-5'
        )
      )
    
    
class GlucoseForm(forms.ModelForm):
  class Meta:
    model = Glucose
    fields = ['glucose_blood', 'glucose_oral', 'created', 'note']
    labels = {
      'glucose_blood': 'Fasting blood sugar test',
      'glucose_oral': 'Oral glucose tolerance test',
    }
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.form_action = ''
    self.helper.attrs = {'id': 'glucoseForm', 'onsubmit': 'formValidation();'}
    self.helper.layout = Layout(
      Field(
        'glucose_blood', placeholder='mg/dL or mmol/L', css_class='js-measurement'
      ),
      Field(
        'glucose_oral', placeholder='mg/dL or mmol/L', css_class='js-measurement'
      ),
      Field(
        'created', placeholder=timezone.now(),
      ),
      Field(
        'note', rows=5, placeholder=' Some info for yourself in the future...', css_class='w-100'
      ),
      ButtonHolder(
        Submit('submit', 'Save', css_class='btn btn-primary'),
        css_class='d-flex justify-content-center mt-2'
      )
    )
    
class GlucoseFormEdit(GlucoseForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper.layout = Layout(
        Field(
          'glucose_blood', placeholder='mg/dL or mmol/L', css_class='js-measurement mb-3'
        ),
        Field(
          'glucose_oral', placeholder='mg/dL or mmol/L', css_class='js-measurement mb-3'
        ),
        Field(
          'created', placeholder=timezone.now(), css_class='mb-3'
        ),
        Field(
          'note', rows=5, placeholder=' Some info for yourself in the future...', css_class='w-100'
        ),
        ButtonHolder(
          Submit('submit', 'Save', onclick="buttonIndex=0;", css_class='btn btn-succes'),
          Submit('delete', 'Delete', onclick="buttonIndex=1;", css_class='btn btn-danger mx-3'),
          HTML('''{% if info %}<p class="align-self-center mb-0 jump-into">{{ info }}</p>{% endif %}'''),
          css_class='d-flex mt-2 mb-5'
        )
      )