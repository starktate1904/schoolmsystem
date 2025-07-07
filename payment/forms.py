from datetime import datetime

from django import forms

from enrollment.models import Enroll
from payment.models import Payment


class CreatePaymentForm(forms.ModelForm):
    enroll_id = forms.ModelChoiceField(
        label='Enrollment',
        queryset=Enroll.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    balance = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        label='Balance',
        required=False
    )
    amount = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label='Amount'
    )
    remarks = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        label='Remarks'
    )
    paid_with = forms.ChoiceField(
        choices=Payment.PAYMENT_METHODS,  # Reference the choices from the Payment model
        label='Paid With',
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial='cash'  # Set default value if needed
    )

    class Meta:
        model = Payment
        fields = ['enroll_id', 'balance', 'amount', 'remarks', 'paid_with']  # Include paid_with in fields


class DateSelectionForm(forms.ModelForm):
    MONTH_CHOICES = (
        (1, "Jan"),
        (2, "Feb"),
        (3, "Mar"),
        (4, "Apr"),
        (5, "May"),
        (6, "Jun"),
        (7, "Jul"),
        (8, "Aug"),
        (9, "Sep"),
        (10, "Oct"),
        (11, "Nov"),
        (12, "Dec"),
    )

    month = forms.ChoiceField(choices=MONTH_CHOICES, initial=datetime.now().month,
                              widget=forms.Select(attrs={'class': 'form-control'}))

    YEAR_CHOICES = []
    for r in range(2020, 2040):
        YEAR_CHOICES.append((r, r))
    year = forms.ChoiceField(choices=YEAR_CHOICES, initial=datetime.now().year,
                             widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Payment
        fields = ['month', 'year']