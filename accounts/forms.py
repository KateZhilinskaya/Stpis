from django import forms
from django.contrib.auth.models import User
from .models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Пароль"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Повторите пароль"}))

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({"placeholder": "Имя", "required": "required"})
        self.fields['last_name'].widget.attrs.update({"placeholder": "Фамилия", "required": "required"})
        self.fields['email'].widget.attrs.update({"placeholder": "Email", "required": "required"})

        for field in self.fields:
            self.fields[field].label = ''

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Пароли не совпадают")
        return cd["password2"]


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ("patronymic", )

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['patronymic'].widget.attrs.update(
            {"placeholder": "Отчество"}
            )

        for field in self.fields:
            self.fields[field].label = ''


class CompanyForm(forms.ModelForm):

    class Meta: 
        model = Company
        fields = ("name", )

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {"placeholder": "Название компании", "required": "required"}
            )

        for field in self.fields:
            self.fields[field].label = ''


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update(
            {"placeholder": "Email", "required": "required"}
        )
        self.fields["password"].widget.attrs.update(
            {"placeholder": "Пароль", "required": "required"}
        )


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("email", )
    
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({"placeholder": "Email", "required": "required"})


class OwnerUserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")

    def __init__(self, *args, **kwargs):
        super(OwnerUserEditForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({"placeholder": "Имя", "required": "required"})
        self.fields['last_name'].widget.attrs.update({"placeholder": "Фамилия", "required": "required"})
        self.fields['email'].widget.attrs.update({"placeholder": "Email", "required": "required"})


class EmployeeForm(forms.ModelForm):

    model = Profile
    class Meta:
        model = Profile
        fields = ("patronymic", "status")

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

        self.fields['patronymic'].widget.attrs.update(
            {"placeholder": "Отчество"}
            )

        for field in self.fields:
            self.fields[field].label = ''