import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from users.forms import RegistrationUserForm, ProfileForm


@pytest.mark.django_db
def test_registration_user_form_valid():
	form_data = {
		"first_name": "test_first_name",
		"last_name": "test_last_name",
		"email": "test_email@example.com",
		"username": "test_username",
		"password1": "dfktynbyf03547",
		"password2": "dfktynbyf03547",
	}

	form = RegistrationUserForm(data=form_data)
	assert form.is_valid()


@pytest.mark.django_db
def test_registration_user_form_invalid():
	form_data = {
		"first_name": "test_first_name",
		"last_name": "test_last_name",
		"email": "test_invalid_email",
		"username": "test_username",
		"password1": "dfktynbyf03547",
		"password2": "dfktynbyf03547",
	}

	form = RegistrationUserForm(data=form_data)
	assert not form.is_valid()
	assert "email" in form.errors


@pytest.mark.django_db
def test_profile_form_valid(create_image):
	form_data = {
		"first_name": "test_first_name",
		"last_name": "test_last_name",
		"email": "test_email@example.com",
	}

	image = create_image
	file_data = {
		"image": SimpleUploadedFile("test_image.jpg", image, content_type="image/jpeg"),
	}

	form = ProfileForm(data=form_data, files=file_data)
	assert form.is_valid()

