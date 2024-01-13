from django import forms
from django.forms import TextInput, EmailInput, NumberInput, Textarea
from .models import Order, Contact
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class OrderForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    class Meta:
        model = Order
        fields = ["amount", "name", "email", "phone", "address", "state", "zip_code"]
        labels = {
            "amount": "Quantity",
            "name": "Name",
            "email": "Email",
            "phone": "Phone",
            "address": "Address",
            "state": "State",
            "zip_code": "Zip code",
        }
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control form-input",
                    "placeholder": "Enter your name",
                }
            ),
            "amount": NumberInput(
                attrs={
                    "class": "form-control form-input",
                    "placeholder": "Enter number of item",
                }
            ),
            "email": EmailInput(
                attrs={
                    "class": "form-control form-input",
                    "placeholder": "Enter your email",
                }
            ),
            "phone": TextInput(
                attrs={
                    "class": "form-control form-input",
                    "placeholder": "Enter phone number with country code",
                }
            ),
            "address": TextInput(
                attrs={
                    "class": "form-control form-input",
                    "placeholder": "Enter your full address",
                }
            ),
            "state": TextInput(
                attrs={
                    "class": "form-control form-input",
                    "placeholder": "Enter state",
                }
            ),
            "zip_code": TextInput(
                attrs={
                    "class": "form-control form-input",
                    "placeholder": "Enter zip code",
                }
            ),
        }


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "message"]
        labels = {
            "name": "Full Name",
            "email": "Email",
            "phone": "Phone",
            "message": "Message",
        }
        widgets = {
            "name": TextInput(
                attrs={
                "id": "name",
                    "class": "form-control input-field",
                    "placeholder": "Enter your name",
                }
            ),
            "email": EmailInput(
                attrs={
                
                    "class": "form-control input-field",
                    "placeholder": "Enter your email",
                }
            ),
            "phone": TextInput(
                attrs={
                    "class": "form-control input-field",
                    "placeholder": "Enter phone number with country code",
                }
            ),
            "message": Textarea(
                attrs={
                    "id": "message",
                    "cols": "60",
                    "rows": "10",
                    "name": "message",
                    "class": "form-control input-field",
                    "placeholder": "Enter your queries here",
                }
            ),
        }
        
