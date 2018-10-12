from django.forms import ModelForm, Form, CharField, PasswordInput
from django import forms

class LoginForm(Form):
    username = CharField(label="User Name", max_length=64)
    password = CharField(widget=PasswordInput())

