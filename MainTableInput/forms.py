from django import forms
from .models import (
    CyberCrime , 
    Victim, 
    Suspect, 
    Investigator 
)

class CyberCrimeForm(forms.ModelForm):
    class Meta:
        model = CyberCrime
        fields = '__all__' 
        
        widgets = {
            'description': forms.Textarea(attrs={'class': 'textarea-input','placeholder':'Write description'}),
            'date_reported': forms.DateInput(attrs={'class': 'date-input','type':'date'}),
        }
        
  

class VictimForm(forms.ModelForm):
    class Meta:
        model = Victim
        fields = '__all__'
        
        widgets = {
            'victim_name': forms.TextInput(attrs={'class': 'textarea-input'}),
            'age': forms.NumberInput(attrs={'class': 'textarea-input','type':'number'}),
            'contact_info' : forms.NumberInput(attrs={'class': 'textarea-input','type':'number'})
        }

class SuspectForm(forms.ModelForm):
    class Meta:
        model = Suspect
        fields = '__all__'
        
        widgets = {
            'suspect_name': forms.TextInput(attrs={'class': 'textarea-input'}),
            'age': forms.NumberInput(attrs={'class': 'textarea-input','type':'number'}),
            'description' : forms.Textarea(attrs={'class': 'textarea-input','type':'number'})
        }
        

class InvestigatorForm(forms.ModelForm):
    class Meta:
        model = Investigator
        fields = '__all__'
        
        widgets = {
            'investigator_name': forms.TextInput(attrs={'class': 'textarea-input'}),
            'badge_number': forms.TextInput(attrs={'class': 'textarea-input'}),
            'contact_info' : forms.NumberInput(attrs={'class': 'textarea-input','type':'number'})
        }
        