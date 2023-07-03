from modulos.scrapy import scrapy
from entidades.Casa import Casa

casa = Casa(
    id=1,
    nome='Sporting Bet',
    slug='sportbet',
    site='https://sports.sportingbet.com/pt-br/sports/'
)

casa.add_esporte(1,'tenis','tênis-5/aposta')
casa.add_esporte(2,'voley', '')

scrapy(casa)