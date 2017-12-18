from django.forms import ModelForm, DateInput
from .models import Event

class DateInput(DateInput):
    input_type = 'date'

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'start': DateInput(),
            'end': DateInput(),            
        }