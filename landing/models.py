from django.db import models


class Inscricao(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Depoimento(models.Model):
    nome = models.CharField(max_length=100)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome