import form as form
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from users.models import User


class RegistrationUserForm(UserCreationForm):
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["last_name", "first_name", "email", "username", "password1", "password2"]


class ProfileForm(UserChangeForm):
	image = forms.ImageField(required=False)

	class Meta:
		model = User
		fields = ["last_name", "first_name", "email", "image"]
