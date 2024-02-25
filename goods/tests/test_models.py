import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_category_str(create_category):
	category = create_category()
	assert str(category) == category.title


@pytest.mark.django_db
def test_product_str(create_product):
	product = create_product()
	assert str(product) == product.title


@pytest.mark.django_db
def test_product_absolute_url(create_product):
	product = create_product()
	expected_url = reverse("catalog:product", kwargs={"slug": product.slug})
	assert product.get_absolute_url() == expected_url


@pytest.mark.django_db
def test_product_display_id(create_product):
	product = create_product()
	assert product.display_id() == f"{product.id:05}"


@pytest.mark.django_db
def test_product_sell_price_with_discount(create_product):
	product = create_product()
	assert product.sell_price() == round(product.price - product.discount * product.price / 100, 2)


@pytest.mark.django_db
def test_product_sell_price_without_discount(create_product):
	product = create_product()
	product.discount = 0.00
	assert product.sell_price() == product.price
