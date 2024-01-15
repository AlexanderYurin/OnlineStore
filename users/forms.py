import form as form
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from users.models import User


class UserLoginForm(AuthenticationForm):
	class Meta:
		model = User


class RegistrationUserForm(UserCreationForm):
	first_name = forms.CharField
	last_name = forms.CharField()
	email = forms.EmailField

	class Meta:
		model = User
		fields = ["last_name", "first_name", "email", "username", "password1", "password2"]
