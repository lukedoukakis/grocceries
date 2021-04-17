from django import forms

class AddressForm(forms.Form):
    value = forms.CharField(widget=forms.TextInput(attrs={'id': 'address'}),label = "street" , max_length = 200)
    