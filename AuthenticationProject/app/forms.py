from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User


############################# custom RegistrationForm for adding custom css class #############
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200,widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":'form-control'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta(forms.ModelForm):
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
        }




######################### Custom AuthenticationForm for adding custom css class ######################
class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,"class":"form-control"}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password","class":"form-control"}),
    )   
    


####################### custom Passwordrestform for adding custom css class ############################
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email",'class':'form-control'}),
    )



######################## custom passwordreset form for adding custom css class ###########################
class CustomPasswordSetForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),
    )
