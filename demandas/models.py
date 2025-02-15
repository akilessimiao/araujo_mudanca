from django.db import models
import json
from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioPersonalizado(AbstractUser):
    nome_completo = models.CharField(max_length=255)
    endereco = models.TextField()
    cpf = models.CharField(max_length=14, unique=True)  # CPF formatado como XXX.XXX.XXX-XX
    telefone = models.CharField(max_length=15)
    is_whatsapp = models.BooleanField(default=False)  # Se o telefone é WhatsApp

# Tabela de referência de pesos (exemplo)
PESOS_REFERENCIA = {
    "geladeira": 60,
    "sofá": 80,
    "máquina de lavar": 70,
    "cama": 50,
    "mesa": 30,
    "cadeira": 10,
    "caixa_pequena": 5,
    "caixa_media": 10,
    "caixa_grande": 15,
}

class Demanda(models.Model):
    nome_cliente = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    descricao = models.TextField(blank=True, null=True)
    itens = models.JSONField()  # Lista de itens em JSON (exemplo: {"geladeira": 1, "sofá": 2})
    peso_estimado = models.FloatField(blank=True, null=True)  # Calculado automaticamente
    data_solicitacao = models.DateTimeField(auto_now_add=True)

    def calcular_peso(self):
        """ Calcula o peso total com base nos itens """
        total_peso = 0
        if self.itens:
            for item, quantidade in self.itens.items():
                total_peso += PESOS_REFERENCIA.get(item, 0) * quantidade
        return total_peso

    def save(self, *args, **kwargs):
        self.peso_estimado = self.calcular_peso()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome_cliente} - {self.peso_estimado}kg"
