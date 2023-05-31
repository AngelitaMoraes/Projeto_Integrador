from django.db import models

# Create your models here.

class Despesa(models.Model):
    categoria_despesa = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return self.categoria_despesa

class Receita(models.Model):
    categoria_receita = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return self.categoria_receita