import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_search_url(client, create_product):
	product = create_product()
	response = client.get(reverse("catalog:search"), data={"q": product.title})
	assert response.status_code == 200
	assert product.title.encode() in response.content


@pytest.mark.django_db
def test_catalog_url(client, create_product):
	product = create_product()
	slug = product.id_category.slug
	response = client.get(reverse("catalog:catalog", kwargs={"cat_slug": slug}))
	assert response.status_code == 200
	assert product.id_category.title.encode() in response.content


@pytest.mark.django_db
def test_product_url(client, create_product):
	product = create_product()
	response = client.get(reverse("catalog:product", kwargs={"slug": product.slug}))
	assert response.status_code == 200


