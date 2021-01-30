from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from gestao_rh import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('empresa/', include('apps.empresas.urls')),
    path('horas-extras/', include('apps.registro_hora_extra.urls')),
    path('documento/', include('apps.documentos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
