import re

class Bet:

    def __init__(self, data, plr1, plr2, odd1, odd2) -> None:
        self.data = data
        self.plr1 = plr1
        self.plr2 = plr2
        self.odd1 = odd1
        self.odd2 = odd2


class Register:

    __regex  = ""
    __plr1I  = -1
    __plr2I  = -1
    __betp1  = -1
    __betp2  = -2
    __dataix = []

    bets=[]

    def __init__(self, regex, player1Index, player2Index, betP1, betP2, dataIndexs) -> None:
        self.__regex  = re.compile(regex)
        self.__plr1I  = player1Index
        self.__plr2I  = player2Index
        self.__betp1  = betP1
        self.__betp2  = betP2
        self.__dataix = dataIndexs

    # dataFunc é a função que vai gerar a data no formato:
    # Y-m-d H:i:s <<-- formato do mysql
    def append(self, content, dataFunc):
        
        res     = self.__regex.match(content)
        groups  = res.groups()
        dataStr = []

        for i in self.__dataix:
            dataStr.append(groups[i])
        data = dataFunc(dataStr)
        
        plr1 = groups[self.__plr1I]
        plr2 = groups[self.__plr2I]
        odd1 = groups[self.__betp1]
        odd2 = groups[self.__betp2]

        self.bets.append((data,plr1,plr2,odd1,odd2))

    def generate(self):
        return [Bet(data,plr1,plr2,odd1,odd2) for data,plr1,plr2,odd1,odd2 in set(self.bets)]
