from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class plano(models.Model):
    nome = models.CharField('Nome', max_length=32)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)
    vendas = models.IntegerField('vendas', validators =[MinValueValidator(0)])

    def __str__(self):
        return self.nome


class cliente(models.Model):
    nome = models.CharField('nome', max_length=64)
    sobrenome = models.CharField('sobrenome', max_length=32)
    email = models.EmailField('email', max_length=100)

    def __str__(self):
        return self.nome