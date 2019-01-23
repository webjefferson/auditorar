from django.db import models


class Loja(models.Model):
    cnpj = models.IntegerField()
    luc = models.IntegerField()
    razaoSocial = models.CharField(max_length=255)

    def __str__(self):
        return self.razaoSocial


class Auditor(models.Model):
    nome = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    loja = models.ManyToManyField(Loja,)


class Triangulacao(models.Model):
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    vendaInformadaLojista = models.DecimalField(max_digits=5, decimal_places=2)
    vendaReducaoz = models.DecimalField(max_digits=5, decimal_places=2)
    vendaAuditoriaPresencial = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField()
