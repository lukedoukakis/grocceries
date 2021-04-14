from django import forms

class AddressForm(forms.Form):
    street = forms.CharField(label = "steet" , max_length = 100)
    city = forms.CharField(label = "city" , max_length = 100)
    zipCode = forms.CharField(label = "zipCode" , max_length = 100)
    