from django import forms
from pcal.models import Member, MemPlan


class MemForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'


class MemPcal(forms.ModelForm):
    class Meta:
        model = MemPlan
        fields = '__all__'
