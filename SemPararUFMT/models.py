from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=500)
    email = models.EmailField(blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome


class CategoriaVeiculo(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return "{} - {:.2f}".format(self.nome, self.preco)


class Veiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    categoria_veiculo = models.ForeignKey(CategoriaVeiculo, on_delete=models.CASCADE)
    placa = models.CharField(max_length=10)
    fabricante = models.CharField(max_length=250, blank=True, null=True)
    modelo = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.placa


class Equipamento(models.Model):
    veiculo = models.OneToOneField(Veiculo, on_delete=models.CASCADE, primary_key=True)
    tag_uid = models.CharField(max_length=20)
    credito = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return "Tag UID: {}, Credito: {}".format(self.tag_uid, self.credito)


class Passagem(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    data = models.DateTimeField()
    valor_passagem = models.DecimalField(max_digits=8, decimal_places=2)
    liberado = models.BooleanField()

    def __str__(self):
        status_msg = "Liberado" if self.liberado else "Recusado"

        return "-----\nPassagem\n{}\n{}\n{}\n{}\nValor: {:.2f}\n{}\n-----" \
            .format(self.equipamento.veiculo.cliente,
                    self.equipamento.veiculo,
                    self.equipamento,
                    self.data, self.valor_passagem, status_msg)
