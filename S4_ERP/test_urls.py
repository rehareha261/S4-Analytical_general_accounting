import pytest
from django.urls import reverse
from django.test import Client
from django.http import HttpResponse

@pytest.fixture
def client():
    """Fixture for Django test client."""
    return Client()

def test_export_pdf_success(client):
    """Test successful access to the export PDF endpoint."""
    url = reverse('export_pdf')
    response = client.get(url)
    assert response.status_code == 200, "Expected status code 200 for successful PDF export"
    assert isinstance(response, HttpResponse), "Expected response to be an instance of HttpResponse"
    assert response['Content-Type'] == 'application/pdf', "Expected content type to be 'application/pdf'"

def test_export_excel_success(client):
    """Test successful access to the export Excel endpoint."""
    url = reverse('export_excel')
    response = client.get(url)
    assert response.status_code == 200, "Expected status code 200 for successful Excel export"
    assert isinstance(response, HttpResponse), "Expected response to be an instance of HttpResponse"
    assert response['Content-Type'] == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', "Expected content type to be 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'"

def test_export_pdf_not_allowed_method(client):
    """Test method not allowed for POST on export PDF endpoint."""
    url = reverse('export_pdf')
    response = client.post(url)
    assert response.status_code == 405, "Expected status code 405 for method not allowed on PDF export"

def test_export_excel_not_allowed_method(client):
    """Test method not allowed for POST on export Excel endpoint."""
    url = reverse('export_excel')
    response = client.post(url)
    assert response.status_code == 405, "Expected status code 405 for method not allowed on Excel export"

def test_export_pdf_invalid_url(client):
    """Test accessing an invalid URL for PDF export."""
    url = '/export/pdf/invalid/'
    response = client.get(url)
    assert response.status_code == 404, "Expected status code 404 for invalid PDF export URL"

def test_export_excel_invalid_url(client):
    """Test accessing an invalid URL for Excel export."""
    url = '/export/excel/invalid/'
    response = client.get(url)
    assert response.status_code == 404, "Expected status code 404 for invalid Excel export URL"