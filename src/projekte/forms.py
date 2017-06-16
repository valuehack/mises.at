from django import forms
from .models import Spenden, Stufen
from django.db.models.signals import pre_save


class StufenModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.betrag
        
        # def __init__(self, projekt, *args, **kwargs):
        #     self.fields['Stufe'].queryset = Stufen.objects.filter(projekt = projekt)

class SpendenModelForm(forms.ModelForm):
    Stufe = StufenModelChoiceField(empty_label = None)
    
    class Meta():
        model = Spenden
        fields = [
            "Vorname",
            "Nachname",
            "Email",
            "Stufe"
        ]
        
    def __init__(self, projekt, *args, **kwargs):
        super(SpendenModelForm, self).__init__(**kwargs)
        self.fields['Stufe'].queryset = Stufen.objects.filter(projekt = projekt)
        # self.fields['Stufe'].empty_label = None
        # self.fields['Stufe'].to_field_name = "betrag"
        print(projekt)
        

def pre_save_receiver(sender, instance, *args, **kwargs):
    instance.Validiert = False
    # instance.Stufe = 


pre_save.connect(pre_save_receiver, sender=Spenden)



#class StufenForm(forms.Form):
#    Stufe = forms.ModelChoiceField(queryset=Stufen.objects.all())
    
# WIE EIN FORM AUS DATENBANKEINTRÄGEN ERZEUGEN?
# WIE BEIDE VERBINDEN?
