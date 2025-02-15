from django.contrib import admin
from django.urls import path, include
from django.urls import path
from .views import cadastro_usuario

urlpatterns = [
    path("cadastro-usuario/", cadastro_usuario, name="cadastro_usuario"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("demandas/", include("demandas.urls")),  # Adiciona as rotas do app "demandas"
]
