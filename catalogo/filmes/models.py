from django.db import models

# Create your models here.
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    ano = models.IntegerField()
    genero = models.CharField()
    capa = models.TextField()

    def __str__(self):
        return self.titulo