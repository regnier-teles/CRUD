from django.db import models


# Create your models here.
class Patrimonios(models.Model):
    ETIQUETA = models.IntegerField()
    RESPONSAVEL = models.CharField(max_length=150)
    CPF_DO_RESPONSAVEL = models.CharField(max_length=15)
    DESCRICAO_DO_EQUIPAMENTO = models.CharField(max_length=150)
    MARCA = models.CharField(max_length=30)
    MODELO = models.CharField(max_length=30)
    NUMERO_DE_SERIE = models.CharField(max_length=30)
    NUMERO_DA_NOTA_FISCAL = models.CharField(max_length=30)
    LOCALIZACAO = models.CharField(max_length=50)
    PROJETO = models.CharField(max_length=150)
    ANO_DO_PROJETO = models.CharField(max_length=4)
    EMPRESA_PATROCINADORA = models.CharField(max_length=150)
