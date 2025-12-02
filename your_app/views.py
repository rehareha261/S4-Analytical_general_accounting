import pandas as pd
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from your_app.models import JournalEntry, FinancialStatement  # Assuming these are your models

def export_report(request):
    report_type = request.POST.get('report_type')
    format_type = request.POST.get('format')
    
    if report_type == 'financial_statement':
        data = FinancialStatement.objects.all().values()
    elif report_type == 'journal_entries':
        data = JournalEntry.objects.all().values()
    else:
        return HttpResponse("Invalid Report Type")

    if format_type == 'pdf':
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{report_type}.pdf"'
        
        p = canvas.Canvas(response)
        p.drawString(100, 100, "This is a test PDF.")
        # Additional PDF generation logic goes here
        p.save()

    elif format_type == 'excel':
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="{report_type}.xlsx"'
        
        df = pd.DataFrame(data)
        with pd.ExcelWriter(response, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Sheet1')

    else:
        return HttpResponse("Invalid Format Type")

    return response