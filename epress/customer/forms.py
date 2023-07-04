from django import forms
from .models import Customer

#CUSTOMER

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['name', 'mobile_number', 'gender']
        labels = {
            'name': 'Customer Name',
            'mobile_number': 'Mobile Number',
            'gender': 'Gender',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 17%;', 'value': '+91'}),
            'gender': forms.Select(choices=Customer.GENDER_CHOICES, attrs={'class': 'form-control'}),
        }

#CUSTOMER