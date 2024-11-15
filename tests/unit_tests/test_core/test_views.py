from django.urls import reverse


def test_home_view(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_view_reverse(client):
    response = client.get(reverse("core:home"))
    assert response.status_code == 200
