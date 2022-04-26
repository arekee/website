from django import forms
from .models import *
from django.forms import ModelForm, TextInput, Textarea, NumberInput,DateInput,PasswordInput


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['name','phone', 'email',  'birthdate','password']

class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["nickname","comment"]
      #  fields = '__all__'
        widgets = {
            "nickname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your nickname'
            }),
            "comment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your comment'
            }),
        }
Gender_Choice= [
    ('male', 'Male'),
    ('female', 'Female'),
        ]
class AddPostForm(forms.Form):
    model = Signup
    name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder':"Enter fullname",'name':"fullname", 'class':'c'}) )
    login = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder':"Enter login",'name':"login", 'class':'c'}) )
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter email",'name':"email", 'class':'c'}) )
    phone = forms.IntegerField( widget=forms.NumberInput(attrs={'placeholder':"Enter phone number",'name':"phonenumber", 'class':'c'}) )
    birthdate = forms.DateTimeField(widget=forms.DateInput(attrs={'placeholder':"Enter Date of birth",'name':"dateofbirth", 'class':'c'}))
    gender = forms.CharField(label='Select your gender',
                             widget=forms.RadioSelect(choices=Gender_Choice))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Enter password",'name':"password", 'class':'c'}))