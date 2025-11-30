import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Journal, EtatFinancier

def export_report(request):
    format = request.POST.get('format')

    if format == 'pdf':
        return export_to_pdf()
    elif format == 'excel':
        return export_to_excel()
    else:
        return HttpResponse('Format non supporté')

def export_to_pdf():
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="rapport.pdf"'

    c = canvas.Canvas(response, pagesize=letter)
    c.drawString(100, 750, "Rapport Financier")
    c.save()

    return response

def export_to_excel():
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="rapport.xlsx"'

    # Dummy data, replace with actual data
    data = {'Account': ['1001', '1002'], 'Name': ['Bank', 'Cash'], 'Balance': [1500, 10000]}
    df = pd.DataFrame(data)

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Rapport')

    return response