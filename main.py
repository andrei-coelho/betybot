import time
from libs.register import Register,Bet
from libs.navigator import Navigator 


register = Register(
    "(\d+\/\d+)\\n(\d+:\d+)\\n([^\\n]+)\\n([^\\n]+)\\n([^\\n]+)\\n([^\\n]+)\\n([^\\n]+)\\n([^\\n]+)\\n([^\\n]+)",
    player1Index=2,
    player2Index=3,
    betP1=7,
    betP2=8,
    dataIndexs=[0,1]
)

def dataGen(dataStr:list):
    return "-".join(dataStr)

register.append("""17/05
16:58
Borna Coric
Fabian Marozsan
AO VIVO
Vencedor
67
1.65
2.27""", dataGen)

register.append("""16/05
16:58
Borna Coric
Fabian Marozsan
AO VIVO
Vencedor
67
1.65
2.27""", dataGen)

register.append("""16/05
16:58
Borna Coric
Fabian Marozsan
AO VIVO
Vencedor
67
1.65
2.27""", dataGen)

print(register.generate())