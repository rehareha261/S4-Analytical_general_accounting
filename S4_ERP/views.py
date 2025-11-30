from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd

def export_pdf(request):
    # Exemple simple de génération de PDF avec des données
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="rapport.pdf"'
    
    # Ajoutez ici la logique de création de fichier PDF
    # Note : Requiert une librairie comme ReportLab pour un PDF détaillé

    return response

def export_excel(request):
    # Exemple d'exportation en Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="rapport.xlsx"'
    
    # Exemple d'utilisation de pandas pour créer un fichier Excel
    df = pd.DataFrame({
        'Colonne 1': [1, 2, 3],
        'Colonne 2': [4, 5, 6],
    })
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)
    
    return response