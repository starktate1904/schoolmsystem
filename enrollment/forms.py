from django import forms

from course.models import Program
from enrollment.models import Enroll
from student.models import Participant


class CreateEnrollForm(forms.ModelForm):
    participant_id = forms.ModelChoiceField(queryset=Participant.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control'}),
                                        label='Participant', initial=1 )

    program_id = forms.ModelChoiceField(queryset=Program.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control'}),
                                       label='Program Name')

    total_fee = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))

    class Meta:
        model = Enroll
        fields = ['participant_id', 'program_id', 'total_fee']
