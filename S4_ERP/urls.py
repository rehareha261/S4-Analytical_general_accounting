from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reactivation/', include('reactivation.urls')),  # Nouveau point de terminaison pour la réactivation
]