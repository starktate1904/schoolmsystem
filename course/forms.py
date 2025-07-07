from django import forms
from course.models import Program, Fee


class CreateprogramForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    level = forms.CharField(label='Level', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    total_amount = forms.FloatField(widget=forms.HiddenInput(), label='Total Amount', required=False)
    program_desc = forms.CharField(label='Description', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'rows': '3'}))

    class Meta:
        model = Program
        fields = ['name', 'level', 'total_amount', 'program_desc']


class CreateFeeForm(forms.ModelForm):
    fee_desc = forms.CharField(label='Description', max_length=100, required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'rows': '3'}))
    amount = forms.FloatField(label='Amount', required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Fee
        fields = ['fee_desc', 'amount']
