from django import forms
from models import Light



class LightForm(forms.ModelForm):
	choices_ =( (1, 'ON'),
			(0,'Off'),
	)
	class Meta:
		
		model = Light
		widgets ={
			'onOff': forms.RadioSelect
		}