from django.test import TestCase
from django.urls import reverse

class ExportReportTest(TestCase):
    def test_export_pdf(self):
        response = self.client.post(reverse('export_report'), {'format': 'pdf'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')

    def test_export_excel(self):
        response = self.client.post(reverse('export_report'), {'format': 'excel'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')