from django import forms
from account_module.models import User
from django.core import validators
from django.core.exceptions import ValidationError

class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'address','about_user']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),
            'about_user': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
            })
        }

        labels = {
            'first_name': 'نام',
            'last_name':'نام خانوادگی',
            'avatar':'تصویر پروفایل',
            'address': 'آدرس'
        }

class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label="کلمه عبور قبلی",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    password = forms.CharField(
        label="کلمه عبور جدید",
        widget=forms.PasswordInput(attrs={
                'class': 'form-control',
            }),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    confirm_password = forms.CharField(
        label="تکرار کلمه عبور جدید",
        widget=forms.PasswordInput(attrs={
                'class': 'form-control',
            }),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        else:
            raise ValidationError('تکرار کلمه عبور جدید با کلمه عبور جدید مغایرت دارد')
