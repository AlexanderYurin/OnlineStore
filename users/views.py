from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic import CreateView, FormView

from carts.models import Cart
from users.forms import RegistrationUserForm, ProfileForm
from users.mixins import MessagesMixin
from users.models import User
from users.utils import get_session_key
from utils.redis_utils import CacheMixin


class RegistrationUser(MessagesMixin, CreateView):
	model = User
	template_name = "users/registration.html"
	form_class = RegistrationUserForm
	messages = "Успешно зарегистрировались"
	success_url = "main:main"

	def form_valid(self, form):
		super().form_valid(form)
		session_key = get_session_key(self.request)
		user = form.instance
		login(self.request, user)
		cart = Cart.objects.filter(session_key=session_key)
		if cart.exists():
			cart.update(user=user)
		return redirect(self.get_success_url())


class LoginUser(CacheMixin, MessagesMixin, LoginView):
	form_class = AuthenticationForm
	template_name = "users/login.html"
	messages = "Добро пожаловать"
	success_url = "main:main"

	def get(self, request, *args, **kwargs):
		ban = self.get_cache(request)
		if ban:
			time = self.get_cache_timeout(request)
			self.messages = f"Бан: {time} секунд! Попробуйте позже"
			return redirect(self.get_success_url())
		return super().get(request, *args, **kwargs)

	def form_valid(self, form):
		cache = self.get_cache(self.request)
		if cache:
			cache.delete(self.get_cache_key(self.request))

		session_key = get_session_key(self.request)
		login(self.request, form.get_user())
		cart = Cart.objects.filter(session_key=session_key)
		if cart.exists():
			cart.update(user=self.request.user)
		return redirect(self.get_success_url())

	def form_invalid(self, form):
		attempts = self.get_cache(self.request)
		if attempts and int(attempts.decode()) >= 3:
			self.set_cache(request=self.request, value="Ban", timeout=self.ban_time)
			time = self.get_cache_timeout(self.request)
			self.messages = f"Бан: {time} секунд! Попробуйте позже"
			return redirect(self.get_success_url())
		if not attempts:
			self.set_cache(request=self.request, value=2)
		else:
			self.set_cache(request=self.request, value=3)
		return super().form_invalid(form)


class LogoutUser(MessagesMixin, LogoutView):
	messages = "Вы вышли из профиля"
	success_url = "main:main"


class ProfileView(LoginRequiredMixin, MessagesMixin, FormView):
	form_class = ProfileForm
	template_name = "users/profile.html"
	success_url = "user:profile"
	messages = "внесены изменения"
	login_url = "user:login"

	def form_valid(self, form):
		form.save()
		return redirect(self.get_success_url())

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update({"instance": self.request.user})
		return kwargs
