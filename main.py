from libs.connector import Connector
from modulos.scrapy import scrapy
from entidades.Casa import Casa

# casas = Connector().query('select * from casas where ativo = 1')

casas = [
    {"id": 1, "nome":"test1", "site":"http://noone1.com.br/", "slug":"umacasa", "ativo":1},
    {"id": 2, "nome":"test2", "site":"http://noone2.com.br/", "slug":"outracasa", "ativo":1},
    {"id": 3, "nome":"test3", "site":"http://noone3.com.br/", "slug":"casaerro", "ativo":1}
]

for c in casas:
    esportes = [
        {
            "id":1,
            "slug":"baseball",
            "uri":"baseball"
        },
        {
            "id":2,
            "slug":"voley",
            "uri":"voley"
        }
    ]
    casa = Casa(
            c['id'],
            c['nome'],
            c['slug'],
            c['site']
        )
    
    for esporte in esportes:
        casa.add_esporte(esporte['id'], esporte['slug'], esporte['uri'])

    scrapy(casa)

# faz o bet aqui