import pytest
from django.test import RequestFactory
from django.urls import reverse
from django.http import HttpResponse
from S4_ERP.views import tableau_de_bord_analytique

@pytest.fixture
def request_factory():
    """Fixture for creating a RequestFactory instance."""
    return RequestFactory()

def test_tableau_de_bord_analytique_view(request_factory):
    """Test that the tableau_de_bord_analytique view returns a 200 response and uses the correct template."""
    request = request_factory.get(reverse('tableau_de_bord_analytique'))
    response = tableau_de_bord_analytique(request)
    
    # Assert that the response is an instance of HttpResponse
    assert isinstance(response, HttpResponse), "Response should be an instance of HttpResponse"
    
    # Assert that the response status code is 200
    assert response.status_code == 200, "Response status code should be 200"
    
    # Assert that the correct template is used
    assert 'analyse/dashboard.html' in [t.name for t in response.templates], "The template used should be 'analyse/dashboard.html'"

def test_tableau_de_bord_analytique_context(request_factory):
    """Test that the context returned by the tableau_de_bord_analytique view is correct."""
    request = request_factory.get(reverse('tableau_de_bord_analytique'))
    response = tableau_de_bord_analytique(request)
    
    # Assert that the context is a dictionary
    assert isinstance(response.context_data, dict), "Context should be a dictionary"
    
    # Assert that the context is empty as expected
    assert response.context_data == {}, "Context should be empty for this view"