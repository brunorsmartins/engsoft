from django.contrib.auth.models import User
from django.db import models

class Sprint(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    atividades = models.IntegerField(default=0)
    equipe = models.IntegerField(default=0)
    comunicacao = models.IntegerField(default=0)
    entregas = models.IntegerField(default=0)
    gerente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sprints')

    def __str__(self):
        return self.nome

    def nota_final(self):
        return (self.atividades + self.equipe + self.comunicacao + self.entregas) / 4

class Daily(models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, related_name='dailys')
    data = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return f"{self.sprint.nome} - {self.data}"
