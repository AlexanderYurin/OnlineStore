import pytest
from PIL import Image
from io import BytesIO

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from goods.models import Categories, Products


@pytest.fixture()
def create_user():
	def _create_user(username="test_username", email="test@example.com",
					 password="dfktynbyf03547", image=None,
					 first_name="test_first_name", last_name="test_last_name"):
		User = get_user_model()
		hashed_password = make_password(password)
		return User.objects.create(username=username, email=email,
								   password=hashed_password, image=image,
								   first_name=first_name, last_name=last_name)

	return _create_user


@pytest.fixture()
def create_image():
	image = Image.new("RGB", (100, 100), color="#FFFFFF")
	image_io = BytesIO()
	image.save(image_io, format="JPEG")
	binary_image_data = image_io.getvalue()
	return binary_image_data
