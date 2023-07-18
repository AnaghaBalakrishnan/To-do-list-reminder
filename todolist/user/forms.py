from typing import Any
from django import forms
from .models import AddReminder
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.


class AddreminderForm(forms.ModelForm):
    class Meta():
        model=AddReminder
        fields='__all__'
        widgets={
            "Caption":forms.TextInput(attrs={"placeholder":"Enter a Caption","class":"form-control"}),
            "reminder_for":forms.TextInput(attrs={"placeholder":"Enter the Reminder","class":"form-control"}),
            "date":forms.DateInput(attrs={"placeholder":"Date","class":"form-control",'type':'date'}),
            "time":forms.TimeInput(attrs={"placeholder":"Time","class":"form-control","type":"time"},),
            "category":forms.Select(attrs={"placeholder":"Select the Category","class":"form-control"})
            
            
            
               
            

        }

class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    email=forms.EmailField()



    def __init__(self, *args: Any, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label='Password'
        self.fields['password2'].label='Password Confirmation'
        self.fields['first_name'].label='First Name'
        self.fields['last_name'].label='Last Name'
        self.fields['username'].label='Username'
        

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["class"] = "form-control"

        self.fields["first_name"].widget.attrs["style"] = "border-radius:13px ; box-shadow: -1px 0px 20px 0px #10165d69; border: solid 2px #217093;  background-color: #f3fafd;"
        self.fields["last_name"].widget.attrs["style"] = "border-radius:13px ; box-shadow: -1px 0px 20px 0px #10165d69; border: solid 2px #217093;  background-color: #f3fafd;"
        self.fields["username"].widget.attrs["style"] = "border-radius:13px ; box-shadow: -1px 0px 20px 0px #10165d69; border: solid 2px #217093;  background-color: #f3fafd;"
        self.fields["password1"].widget.attrs["style"] = "border-radius:13px ; box-shadow: -1px 0px 20px 0px #10165d69; border: solid 2px #217093;  background-color: #f3fafd;"
        self.fields["password2"].widget.attrs["style"] = "border-radius:13px ; box-shadow: -1px 0px 20px 0px #10165d69; border: solid 2px #217093;  background-color: #f3fafd;"
        


        self.fields['password1'].help_text=None
        self.fields['password2'].help_text=None
    
    class Meta():
        model=User
        fields=['first_name','last_name','username','email','password1','password2']
        help_texts={
            'username' : None
        }

class LoginForm(forms.Form):
   username=forms.CharField(max_length=100)
   password=forms.CharField(max_length=12,widget=forms.PasswordInput())
   
 




