from django import forms
from useraccount.models import User,Profile
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = "__all__"
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        for f in self.visible_fields():
            f.field.widget.attrs["class"] = "form-control"

class CustomSignUpForm(UserCreationForm):
    email = forms.EmailField()

    def cleaned_password_1(self):
        password = self.cleaned_data.get("password1")
        if len(password) < 10:
            raise VaiidationError("Password must contain 10 characters.")
        return password

    
 