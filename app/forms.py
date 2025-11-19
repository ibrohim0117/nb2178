from django.forms import ModelForm, Form, CharField, PasswordInput
from django.contrib.auth.hashers import make_password
from .models import Users


class UserRegisterForm(ModelForm):
    class Meta: 
        model = Users
        fields = ['username', 'password', 'first_name']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return make_password(password)
    

class UserLoginForm(Form):
    username = CharField(max_length=100)
    password = CharField(widget=PasswordInput)