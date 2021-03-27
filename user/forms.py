from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from django.db import transaction
from .models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class RegistrationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model 		= User
		fields 		= ['email', 'password1','password2']


