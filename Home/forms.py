from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book, Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'isbn')


class SignUpForm(UserCreationForm):
    err = {
        'required': 'You must type a name !',
    }
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.',error_messages=err)
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    Phone = forms.IntegerField()
    School = forms.CharField(max_length=254)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class LoginForm(forms.Form):

    email = forms.CharField()
    password = forms.CharField()

    def clean(self):
        cleaned_data = self.cleaned_data
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if not email and not password:
            raise forms.ValidationError(u'Please enter the required information')
        elif User.objects.get(email=email).check_password(password):
            return cleaned_data
        else:
            raise forms.ValidationError(u'Incorrect email or password')
