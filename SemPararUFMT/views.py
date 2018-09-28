from decimal import *

from django.http import HttpResponse
from django.utils import timezone

from .models import *


def check_passagem(request, tag_uid):
    passagem_liberada = fazer_passagem(tag_uid)

    if passagem_liberada:
        msg = "Liberado"
        status = 200  # Status OK
    else:
        msg = "Recusado"
        status = 403  # Status Recusado

    return HttpResponse(msg, status=status)


def fazer_passagem(tag_uid):
    equipamento = Equipamento.objects.filter(tag_uid=tag_uid)[0]
    preco_categoria = equipamento.veiculo.categoria_veiculo.preco

    credito_subtraido = False
    if equipamento.credito >= preco_categoria:
        equipamento.credito = Decimal(equipamento.credito) - preco_categoria
        credito_subtraido = True
        equipamento.save()

    passagem = Passagem(
        equipamento=equipamento,
        data=timezone.now(),
        valor_passagem=preco_categoria,
        liberado=credito_subtraido
    )
    passagem.save()

    print(passagem)
    return passagem.liberado


def index(request):
    return HttpResponse("Hello world")
