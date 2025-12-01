import pytest
from django.http import HttpRequest
from reactivation.views import index

@pytest.fixture
def mock_request():
    """Fixture to create a mock HttpRequest object."""
    return HttpRequest()

def test_index_returns_httpresponse(mock_request):
    """Test that the index function returns an HttpResponse object."""
    response = index(mock_request)
    assert isinstance(response, HttpResponse), "Expected an HttpResponse object"

def test_index_response_content(mock_request):
    """Test that the index function returns the correct content."""
    response = index(mock_request)
    expected_content = "Bienvenue sur la page de réactivation!"
    assert response.content.decode() == expected_content, f"Expected content to be '{expected_content}'"

def test_index_response_status_code(mock_request):
    """Test that the index function returns a 200 status code."""
    response = index(mock_request)
    assert response.status_code == 200, "Expected status code to be 200"