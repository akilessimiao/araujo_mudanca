from django.urls import path
from .views import formulario_demanda  # Importa a view corretamente

urlpatterns = [
    path("cadastro/", formulario_demanda, name="cadastro"),
]
