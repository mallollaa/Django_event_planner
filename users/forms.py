from django import forms
from django.contrib.auth import get_user_model
User = get_user_model() 

class RegisterForm(forms.ModelForm):
	class Meta :
            model = User
            fields = ['username','email','password']
        #these are the defaults in the admin dashboard 
         # we will pass what we want to costume 
            Widgets = {
          # this is to make the pass hidden 
                "password": forms.PasswordInput()
                }
        # it's for hiding the password 

        #this is for users to be able to login 
class LoginForm(forms.Form):
    username =forms.CharField(required = True)
    password =forms.CharField(widget = forms.PasswordInput(),required = True)