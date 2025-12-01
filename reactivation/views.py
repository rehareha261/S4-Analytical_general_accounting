from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenue sur la page de réactivation!")