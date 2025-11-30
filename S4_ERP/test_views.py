import pytest
from django.http import HttpRequest
from .views import export_pdf, export_excel

@pytest.fixture
def mock_request():
    """Fixture to create a mock HttpRequest object."""
    return HttpRequest()

def test_export_pdf_content_type(mock_request):
    """Test that export_pdf returns a response with the correct PDF content type."""
    response = export_pdf(mock_request)
    assert response['Content-Type'] == 'application/pdf', "Content-Type should be 'application/pdf'"

def test_export_pdf_content_disposition(mock_request):
    """Test that export_pdf returns a response with the correct content disposition for attachment."""
    response = export_pdf(mock_request)
    assert response['Content-Disposition'] == 'attachment; filename="rapport.pdf"', \
        "Content-Disposition should be 'attachment; filename=\"rapport.pdf\"'"

def test_export_excel_content_type(mock_request):
    """Test that export_excel returns a response with the correct Excel content type."""
    response = export_excel(mock_request)
    assert response['Content-Type'] == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', \
        "Content-Type should be 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'"

def test_export_excel_content_disposition(mock_request):
    """Test that export_excel returns a response with the correct content disposition for attachment."""
    response = export_excel(mock_request)
    assert response['Content-Disposition'] == 'attachment; filename="rapport.xlsx"', \
        "Content-Disposition should be 'attachment; filename=\"rapport.xlsx\"'"

def test_export_excel_content(mock_request):
    """Test that export_excel returns a response with valid Excel content."""
    response = export_excel(mock_request)
    # Check if the response content is not empty
    assert response.content, "The Excel file content should not be empty"
    # Further checks can be done by parsing the content with openpyxl or similar library

# Note: Since the PDF generation logic is not implemented, we cannot test the actual PDF content.