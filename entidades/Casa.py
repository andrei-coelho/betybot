
from entidades.Esporte import Esporte

class Casa:

    def __init__(self, id, nome, slug, site):
        self.id   = id
        self.nome = nome
        self.slug = slug
        self.site = site
        self.esportes=[]
    
    def add_esporte(self,id, slug, uri):
        self.esportes.append(Esporte(id=id, slug=slug, link=self.site+uri))