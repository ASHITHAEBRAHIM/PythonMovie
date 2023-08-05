from django import forms
from .models import actors

class actorsform(forms.ModelForm):
    class Meta:
        model = actors
        fields = ['Name','Age','Desc','Image']
