from django.db import models

class Ator(models.Model):
    nome = models.CharField(max_length=80)
    idade = models.CharField(max_length=20)
    personagem = models.CharField(max_length=80)
    nascimento = models.DateField()
    imagem = models.ImageField(upload_to='imagens/')
    conteudo = models.CharField(max_length=2000)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Atores"


class Elenco(models.Model):
    imagem_e = models.ImageField(upload_to='imagens/')

    
