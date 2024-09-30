from django.contrib.auth.models import User
from django.db import models

class Sprint(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    gerente = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Campos de avaliação
    atividades = models.IntegerField(default=0)
    equipe = models.IntegerField(default=0)
    comunicacao = models.IntegerField(default=0)
    entregas = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

    def calcular_media(self):
        """Calcula a média das notas de todas as Dailys associadas."""
        dailys = self.daily_set.all()
        if dailys:
            total_notas = sum([daily.nota for daily in dailys])
            return total_notas / dailys.count()
        return 0

    @property
    def nota_final(self):
        """Propriedade para calcular a nota final da Sprint."""
        return self.calcular_media()

class Daily(models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    descricao = models.TextField()
    data = models.DateField()
    nota = models.IntegerField()

    def __str__(self):
        return f"Daily {self.data} - {self.nota}/100"
