import time
from libs.register import Register
from libs.navigator import Navigator 

navegador=Navigator(site="https://br.betano.com/sport/tenis/ligas/16907r,16907o,16756r,16756o/")

#time.sleep(60)
# (\d+\/\d+)\n(\d+:\d+)\n([^\n]+)\n([^\n]+)\n([^\n]+)\n([^\n]+)\n([^\n]+)\n([^\n]+)\n([^\n]+)
#  0 -> data
#  1 -> hora
#  2 -> player1
#  3 -> player2
#  7 -> bet1
#  8 -> bet2  #
# print(navegador.findElement('class', 'events-list__grid__event').innerText())

register = Register(
    "(\d+\/\d+)\\n(\d+:\d+)\\n([^\\n]+)\\n([^\\n]+)\\n([^\\n]+)\\n([^\\n]+)\\n([^\\n]+)\\n([^\\n]+)\\n([^\\n]+)",
    player1Index=2,
    player2Index=3,
    betP1=7,
    betP2=8,
    dataIndexs=[0,1]
)

def dataGen(dataStr):
    print(dataStr)

register.append("""16/05
16:58
Borna Coric
Fabian Marozsan
AO VIVO
Vencedor
67
1.65
2.27""", dataGen)