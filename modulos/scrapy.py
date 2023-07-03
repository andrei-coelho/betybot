from libs.connector import Connector
from libs.register import Bet
import os

def import_from(module, name):
    module = __import__(module, fromlist=[name])
    return getattr(module, name)

def scrapy_sport(casa, modesport=False):
    if not modesport:
        try:
            scrapmod = import_from('scrapers.'+casa.slug, 'script_func') 
        except:
            print("O script '"+casa.slug+".py' não foi definido corretamente")
            return
    for esporte in casa.esportes:
        if modesport:
            try:
                scrapmod = import_from('scrapers.'+casa.slug+'.'+esporte.slug, 'script_func') 
            except:
                print("O script '"+casa.slug+"/"+esporte.slug+".py' não foi definido corretamente")
                continue
        bets:list[Bet] = scrapmod(esporte)
        print(bets)


def scrapy(casa):
    modesport = True if os.path.isdir('scrapers/'+casa.slug) else False
    scrapy_sport(casa=casa,modesport=modesport)
    
