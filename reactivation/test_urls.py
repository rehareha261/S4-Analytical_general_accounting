import pytest
from django.urls import reverse
from django.test import Client
from django.http import HttpResponseNotFound

@pytest.fixture
def client():
    """Fixture for Django test client."""
    return Client()

def test_index_view_status_code(client):
    """
    Test that the index view returns a 200 status code.
    """
    response = client.get(reverse('index'))
    assert response.status_code == 200, "Index view should return status code 200"

def test_index_view_content(client):
    """
    Test that the index view returns the expected content.
    """
    response = client.get(reverse('index'))
    assert b"Welcome to the index page" in response.content, "Index view should contain welcome message"

def test_index_view_not_found(client):
    """
    Test that accessing a non-existent URL returns a 404 status code.
    """
    response = client.get('/non-existent-url/')
    assert isinstance(response, HttpResponseNotFound), "Non-existent URL should return 404 status code"