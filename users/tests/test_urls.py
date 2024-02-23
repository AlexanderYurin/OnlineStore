import pytest
from django.urls import reverse


def test_login_user():
	pass


def test_registration_user():
	pass


def test_profile_user_auth():
	pass


def test_profile_user_not_auth(client):
	url = reverse("users:profile")
	response = client.get(url)
	assert response.status_code == 302
	assert "user/login/" in response.url


def test_logout_user():
	pass


def test_user_cart():
	pass
