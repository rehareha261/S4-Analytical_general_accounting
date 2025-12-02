import pytest
from django.http import HttpRequest, HttpResponse
from django.test import RequestFactory
from unittest.mock import patch, MagicMock
from your_app.views import export_report

@pytest.fixture
def request_factory():
    return RequestFactory()

@pytest.fixture
def mock_financial_statement():
    with patch('your_app.views.FinancialStatement.objects.all') as mock:
        yield mock

@pytest.fixture
def mock_journal_entry():
    with patch('your_app.views.JournalEntry.objects.all') as mock:
        yield mock

def test_export_report_financial_statement_pdf(request_factory, mock_financial_statement):
    # Arrange
    request = request_factory.post('/', data={'report_type': 'financial_statement', 'format': 'pdf'})
    mock_financial_statement.return_value.values.return_value = [{'id': 1, 'name': 'Statement 1'}]

    # Act
    response = export_report(request)

    # Assert
    assert isinstance(response, HttpResponse)
    assert response['Content-Type'] == 'application/pdf'
    assert 'attachment; filename="financial_statement.pdf"' in response['Content-Disposition']

def test_export_report_journal_entries_excel(request_factory, mock_journal_entry):
    # Arrange
    request = request_factory.post('/', data={'report_type': 'journal_entries', 'format': 'excel'})
    mock_journal_entry.return_value.values.return_value = [{'id': 1, 'entry': 'Entry 1'}]

    # Act
    response = export_report(request)

    # Assert
    assert isinstance(response, HttpResponse)
    assert response['Content-Type'] == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    assert 'attachment; filename="journal_entries.xlsx"' in response['Content-Disposition']

def test_export_report_invalid_report_type(request_factory):
    # Arrange
    request = request_factory.post('/', data={'report_type': 'invalid_type', 'format': 'pdf'})

    # Act
    response = export_report(request)

    # Assert
    assert isinstance(response, HttpResponse)
    assert response.content.decode() == "Invalid Report Type"

def test_export_report_invalid_format_type(request_factory, mock_financial_statement):
    # Arrange
    request = request_factory.post('/', data={'report_type': 'financial_statement', 'format': 'invalid_format'})
    mock_financial_statement.return_value.values.return_value = [{'id': 1, 'name': 'Statement 1'}]

    # Act
    response = export_report(request)

    # Assert
    assert isinstance(response, HttpResponse)
    assert response.content.decode() == "Invalid Format Type"