from django import forms

from curdapp.models import CrudView

class CrudForm(forms.ModelForm):
    class Meta:
        model = CrudView 
        fields = '__all__'