from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
<<<<<<< HEAD
from django.contrib.auth import authenticate
=======
>>>>>>> 4710397c97df0ed639ec731e8792e78cf5f126f4

User = get_user_model()



<<<<<<< HEAD
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
=======
class RegisterationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

    def clean_email(self):
        '''Verify email is available'''
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('email is taken')
        return email
    
    def clean(self):
        '''Verify both passwords match.'''
        cleaned_data = super(RegisterationForm, self).clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password is not None and password != password2:
            self.add_error('password2', 'Your passwords must match')
        return cleaned_data
    
    def save(self, commit=True):
        '''Save the provided password in hashed format'''
        user = super().save(commit=False)
>>>>>>> 4710397c97df0ed639ec731e8792e78cf5f126f4
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

<<<<<<< HEAD
class UserAdminCreationForm(forms.ModelForm):
    """The form is used for creating a new user. Including all the required fields, also a repeted password."""
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
=======

class UserAdminCreationForm(forms.ModelForm):
    '''A form for creating new users. Includes all the required fields, plus  a repeated password.'''
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
>>>>>>> 4710397c97df0ed639ec731e8792e78cf5f126f4

    class Meta:
        model = User
        fields = ['email']
<<<<<<< HEAD
    
    def clean(self):
        """Verify both passwords match"""
=======

    def clean(self):
        '''Verify both password match.'''
>>>>>>> 4710397c97df0ed639ec731e8792e78cf5f126f4
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password is not None and password != password2:
<<<<<<< HEAD
            raise self.add_error('Password2', 'Your password must match')
        return cleaned_data
    
    def save(self, commit=True):
        """Save the password in hash format."""
        user = super(RegistrationForm, self).save(commit=False)
=======
            self.add_error('password2', 'Your passwords must match.')
        return cleaned_data

    def save(self, commit=True):
        '''Save the provided password in hashed format'''
        user = super().save(commit=False)
>>>>>>> 4710397c97df0ed639ec731e8792e78cf5f126f4
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
<<<<<<< HEAD
    

class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on the user, but replaces the password with admin's password hash display field"""
=======

class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on the user, but replaces the password field with admin's password hash display field"""
>>>>>>> 4710397c97df0ed639ec731e8792e78cf5f126f4
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
<<<<<<< HEAD
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
=======
        fields = ['email', 'password', 'active', 'admin']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial['password']
>>>>>>> 4710397c97df0ed639ec731e8792e78cf5f126f4
