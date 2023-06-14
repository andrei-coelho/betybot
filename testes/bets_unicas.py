from libs.register import Register,Bet
from libs.navigator import Navigator 

lista:list = [
    (1, "andrei"),
    (1, "andreif"),
    (2, "gu"),
    (2, "gu"),
]

lista = [Bet(id, nome) for id,nome in set(lista)]
