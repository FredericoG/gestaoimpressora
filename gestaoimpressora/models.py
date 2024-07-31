from django.db import models

# Create your models here.

class Equipamento(models.Model):
    MAQUINA_MAX_LENGTH = 100
    SERIAL_MAX_LENGTH = 100

    TURNOS = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('ambos', 'Ambos os turnos')
    ]

    TIPOS = [
        ('colorido', 'Colorido'),
        ('pb', 'Preto & Branco')
    ]

    maquina = models.CharField(max_length=MAQUINA_MAX_LENGTH, blank=False, null=False)
    serial = models.CharField(max_length=SERIAL_MAX_LENGTH, blank=False, null=False)
    tipoeqipopcoes = models.CharField(max_length=20, choices=TIPOS)
    paginaminuto = models.PositiveIntegerField(blank=False, null=False)
    opcaoturno = models.CharField(max_length=20, choices=TURNOS)
    capacidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.maquina} ({self.serial})"
    


class Contador(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    contador = models.PositiveIntegerField()
    data = models.DateField()

    def __str__(self):
        return f"{self.equipamento.descricao} - {self.contador}"


class Item(models.Model):
    TIPOS = [
        ('peca', 'Peça'),
        ('insumo', 'Insumo')
    ]

    codigo = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    descricao = models.CharField(max_length=255)
    custo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    durabilidade = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.codigo


class Troca(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    contador = models.PositiveIntegerField()
    data_troca = models.DateField()

    def __str__(self):
        return f"Troca de {self.item.descricao} no equipamento {self.equipamento.descricao}"