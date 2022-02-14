from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate

User = get_user_model()



class RegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control'
    }))
    password2 = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control'
    }))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


    def clean_email(self):
        """Verify email is unique?"""
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email already taken')
        return email


    def clean(self):
        '''Verify both passwords match'''
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password is not None and password != password2:
            raise self.add_error('Password2', 'Your password must match')
        return cleaned_data

    def save(self, commit=True):
        """Save the password in hash format."""
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserAdminCreationForm(forms.ModelForm):
    """The form is used for creating a new user. Including all the required fields, also a repeted password."""
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']
    
    def clean(self):
        """Verify both passwords match"""
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password is not None and password != password2:
            raise self.add_error('Password2', 'Your password must match')
        return cleaned_data
    
    def save(self, commit=True):
        """Save the password in hash format."""
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    

class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on the user, but replaces the password with admin's password hash display field"""
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'password', 'admin']

    def clean_password(self):
        """Regardlass of what user provides, return the initial value. This is done here, rather than on the field, because the field does not have access to the initial field"""
        return self.initial['password']

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
            'class': 'form-control',
        }
    ))


    class Meta:
        model = User
        fields = ['email', 'password']


    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['email'].widget.attrs['class'] = 'form-control'

    
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Cridential')