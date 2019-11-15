from django import forms
from . import models

class CreateCustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['FirstName', 'LastName', 'Email', 'Phone',
                    'Address', 'City', 'Pincode']
