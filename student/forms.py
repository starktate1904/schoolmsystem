from django import forms
from .models import Participant  # Make sure to import your Participant model

class CreateparticipantForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    contact = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=200, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': '3'
    }))
    gender = forms.ChoiceField(
        choices=Participant.GENDER_CHOICES,widget=forms.Select(attrs={'class':'form-control'}),
        label='Gender'
    )
    next_of_kin = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    next_of_kin_number = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date'  # This will render a date picker in modern browsers
    }))
    
    # Add the disciplinary_case field
    disciplinary_case = forms.ChoiceField(
        choices=Participant.DISCIPLINARY_CASE_CHOICES,  # Reference the choices from the Participant model
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Disciplinary Case'
    )
    

    class Meta:
        model = Participant
        fields = ['name', 'email', 'contact', 'address', 'next_of_kin', 'next_of_kin_number', 'date_of_birth', 'disciplinary_case','gender']