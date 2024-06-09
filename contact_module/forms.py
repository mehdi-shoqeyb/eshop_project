from django import forms
from .models import ContactUs

from django.core import validators

class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'نام و نام خانوادگی'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'ایمیل'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'عنوان'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'id': 'message',
                'placeholder':'متن پیام'
            })
        }

        labels = {
            'full_name': 'نام و نام خانوادگی شما',
            'email': 'ایمیل شما'
        }
        placeholder ={}
        error_messages = {
            'full_name': {
                'required': 'نام و نام خانوادگی اجباری می باشد. لطفا وارد کنید'
            }
        }

class ProfileForm(forms.Form):
    user_image = forms.ImageField()