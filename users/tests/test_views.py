import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse


@pytest.mark.django_db
def test_login_user(create_user, client):
	user = create_user()
	url = reverse("users:login")
	response = client.get(url)
	assert response.status_code == 200
	user_data = {"username": user.username, "password": "dfktynbyf03547"}
	response = client.post(url, data=user_data)
	assert response.status_code == 302
	assert reverse("main:main") in response.url


@pytest.mark.django_db
def test_registration_user(client):
	url = reverse("users:registration")
	response = client.get(url)
	assert response.status_code == 200

	form_data = {
		"first_name": "test_first_name",
		"last_name": "test_last_name",
		"email": "test_email@example.ru",
		"username": "test_username",
		"password1": "dfktynbyf03547",
		"password2": "dfktynbyf03547",
	}

	response = client.post(url, data=form_data)
	assert response.status_code == 302
	assert reverse("main:main") in response.url
	user = get_user_model().objects.filter(username=form_data["username"])
	assert len(user) == 1


@pytest.mark.django_db
def test_profile_user_auth(create_user, client):
	user = create_user()
	login = client.login(username=user.username, password="dfktynbyf03547")
	assert login is True
	url = reverse("user:profile")
	response = client.get(url)
	assert response.status_code == 200


def test_profile_user_not_auth(client):
	url = reverse("users:profile")
	response = client.get(url)
	assert response.status_code == 302
	assert reverse("users:login") in response.url


@pytest.mark.django_db
def test_logout_user(create_user, client):
	user = create_user()
	login = client.login(username=user.username, password="dfktynbyf03547")
	url = reverse("users:logout")
	response = client.post(url)
	assert response.status_code == 302
	assert reverse("main:main") in response.url


@pytest.mark.django_db
def test_user_cart(create_user, client):
	user = create_user()
	login = client.login(username=user.username, password="dfktynbyf03547")
	url = reverse("users:user_cart")
	response = client.get(url)
	assert response.status_code == 200

