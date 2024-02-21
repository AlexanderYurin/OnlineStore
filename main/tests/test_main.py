import pytest
from django.urls import reverse, NoReverseMatch


@pytest.mark.django_db
def test_view_unauthorized(client):
    url = reverse("main:main")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_as_admin(client):
    url = reverse("main:about")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_invalid_url(client):
    with pytest.raises(NoReverseMatch):
        url = reverse("main:home")
        response = client.get(url)


