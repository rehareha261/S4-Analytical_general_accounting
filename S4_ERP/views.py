from django.shortcuts import render

def tableau_de_bord_analytique(request):
    # Vous pourriez récupérer des données ici à partir des modèles
    context = {}
    return render(request, 'analyse/dashboard.html', context)