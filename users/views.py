from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegistrationUserForm
from users.models import User


# Create your views here.

class RegistrationUser(CreateView):
	model = User
	template_name = "users/registration.html"
	form_class = RegistrationUserForm

	def form_valid(self, form):
		form.save()
		user = form.instance
		login(self.request, user)
		return redirect("main:main")


class LoginUser(LoginView):
	form_class = AuthenticationForm
	template_name = "users/login.html"

	def get_success_url(self):
		return reverse_lazy("main:main")


class LogoutUser(LogoutView):
	def get_success_url(self):
		return reverse_lazy("main:main")


def profile(request):
	context = {
		"title"
	}
	return render(request, "users/profile.html")


def registration(request):
	context = {
		"title"
	}
	return render(request, "users/registration.html")
