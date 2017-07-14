from django import forms
from .models import Spenden, Stufen
from django.db.models.signals import pre_save
import pprint


class StufenModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return str(obj.betrag) + "€"

class SpendenModelForm(forms.ModelForm):
    Vorname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Vorname'}))
    Nachname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nachname'}))
    Email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    
    class Meta():
        model = Spenden
        fields = [
            "Vorname",
            "Nachname",
            "Email",
            "Stufe"
        ]
        
    Stufe = StufenModelChoiceField(queryset=Stufen.objects.all(), empty_label="Stufe wählen")
        
    def __init__(self, projekt, *args, **kwargs):
        super(SpendenModelForm, self).__init__(*args, **kwargs)
        self.fields['Stufe'].queryset = Stufen.objects.filter(projekt = projekt)
