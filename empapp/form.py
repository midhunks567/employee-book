from .models import Emp
from django import forms

class Empforms(forms.ModelForm):
    class Meta:
        model=Emp
        fields=['name','emp_id','occup']