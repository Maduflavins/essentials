from django import forms
from .models import Order

class OrederCreateForm(forms.ModelForm):
    class Meta:
        fields = ['first_name', 'last_name', 'email', 'adderess', 'postal_code', 'city']