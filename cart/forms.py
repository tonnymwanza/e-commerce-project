from django import forms
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from . models import Profile, CartItem
from . validators import email_validation

class CartItemsForm(forms.Form):
    City = (
        ('nrb', 'Nairobi'),
        ('mbs', 'Mombasa'),
        ('ksm', 'Kisumu'),
        ('eldy', 'Eldorect')
    )
    Constituency = (
        ('dgts', 'Dagoretti south'),
        ('dgtn', 'Dagoretti north'),
        ('thk', 'Thika'),
        ('kmb', 'Kiambu'),
        ('ktl', 'Kitengela'),
        ('kky', 'kikuyu'),
        ('klm', 'Kilimani')
    )
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=40)
    phone_number = forms.IntegerField()
    email = forms.EmailField(validators = [email_validation])
    address1 = forms.CharField(max_length=255)
    address2 = forms.CharField(max_length=255)
    city = forms.CharField(widget=forms.RadioSelect(choices=City))
    country = CountryField()
    postal_code = forms.IntegerField()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email'
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'location'
        ]