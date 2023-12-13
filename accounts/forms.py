from typing import Any
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blogapp.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=('bio','profile_pic','facebook_url','instagram_url','linkedin_url','github_url')
        widgets={
                'bio':forms.Textarea(attrs={'class':'form-control'}),
                # 'profile_pic':forms.ImageField(attrs={'class':'form-control'}),
                'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
                'instagram_url':forms.TextInput(attrs={'class':'form-control'}),
                'linkedin_url':forms.TextInput(attrs={'class':'form-control'}),
                'github_url':forms.TextInput(attrs={'class':'form-control'}),
            }


class SignupForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),label='Email')
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}),label='First Name')
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}),label='Last Name')
    phone_no=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}),label='Phone Number')
    
    class Meta:
        model = User
        fields=('username','first_name','last_name','phone_no','email','password1','password2')
        
    def __init__(self, *args, **kwargs):
        super(SignupForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'

class EditSignupForm(UserChangeForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),label='Email')
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}),label='First Name')
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}),label='Last Name')
    phone_no=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}),label='Phone Number')
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}),label='Username')
    last_login=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    is_superuser=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_stuff=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields=('username','first_name','last_name','phone_no','email','password','last_login','is_superuser','is_stuff','is_active','date_joined')
  
class PasswordChangingForm(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}),label='Old Password')
    new_password1=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}),label='Enter New Password')
    new_password2=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}),label='New Password(Again)')
    
    class Meta:
        model = User
        fields=('old_password','new_password1','new_password2')
      