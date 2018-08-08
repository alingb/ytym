from django.forms import ModelForm
from web.models import Stat
from django import forms
class AddForm(ModelForm):
    class Meta:
        model = Stat
        fields = '__all__'

class Update(forms.Form):
    #CHOISE = (("bios", "one"), ("bmc", "two"), ("fru", "three"))
    #choise = forms.MultipleChoiceField(choices=CHOISE, widget=forms.CheckboxSelectMultiple())
    filename = forms.FileField()
    
