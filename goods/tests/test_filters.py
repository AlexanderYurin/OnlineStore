import pytest

from goods.filters import query_search


@pytest.mark.django_db
def test_query_search_isdigit(create_product):
	product = create_product()
	data = query_search("1")
	assert product.id == data.first().id


@pytest.mark.django_db
def test_query_search_title(create_product):
	product = create_product()
	data = query_search("Test Product")
	assert product.id == data.first().id


@pytest.mark.django_db
def test_query_search_description(create_product):
	product = create_product()
	data = query_search("Test Description")
	assert product.id == data.first().id


@pytest.mark.django_db
def test_query_search_not_value(create_product):
	product = create_product()
	data = query_search("Диван")
	assert len(data) == 0
