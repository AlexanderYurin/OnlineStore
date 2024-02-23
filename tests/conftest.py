import pytest
from django.contrib.auth import get_user_model

from goods.models import Categories, Products


@pytest.fixture(scope="module")
def create_category():
    def _create_category(title="Test Category", slug="test-category"):
        return Categories.objects.create(title=title, slug=slug)
    return _create_category


@pytest.fixture(scope="module")
def create_product(create_category):
    def _create_product(title="Test Product", slug="test-product", category=None):
        if not category:
            category = create_category()
        return Products.objects.create(
                slug=f"test-product",
                title=f"Test Product",
                description="Test Description",
                image="path/to/image.jpg",
                quantity=10,
                price=20.00,
                discount=5.00,
                id_category=category
            )

    return _create_product


@pytest.fixture(scope="module")
def create_user():
    def _create_user(username="test_user", email="test@example.com",
					 password="password", image=None,
					 first_name="test_first_name", last_name="test_last_name"):
        User = get_user_model()
        return User.objects.create(username=username, email=email,
								   password=password, image=image,
								   first_name=first_name, last_name=last_name)

    return _create_user

