from django import forms
from django.forms import ModelForm
from . models import Customer



# A form for capturing a new record
class RecordsForm(ModelForm):
	class Meta:
		model = Customer
		fields = ('first_name','last_name','phone','email','city','date')
		labels = {
			'first_name': '',
			'last_name': '',
			'phone': '',
			'email': '',
			'city': '',
			'date': 'mm/dd/yyyy',
		}
		widgets = {
			'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
			'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
			'date': forms.TextInput(attrs={'class':'form-control','placeholder':'Date'}),
			'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
			'city': forms.TextInput(attrs={'class':'form-control', 'placeholder':'County'}),
			'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
		}