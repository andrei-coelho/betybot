from libs.connector import Connector
from libs.register import Bet

def import_from(module, name):
    module = __import__(module, fromlist=[name])
    return getattr(module, name)

def scrapy(casa):
    try:
        scrapmod = import_from('scrapers.'+casa.slug, 'script_func')
        
        for esporte in casa.esportes:
            bets:list[Bet] = scrapmod(esporte)
            print(bets)
    except:
        print("O script 'scrapers/"+casa.slug+".py' nao foi definido corretamente.")
        