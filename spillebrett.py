import random
from celle import Celle

class Spillebrett:
    def __init__(self , rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._gnNr = 0
        self._rutenett = []
        nyCelle = Celle()
        for i in range(self._rader):
            liste = []
            for e in range(self._kolonner):
                liste.append(nyCelle)
            self._rutenett.append(liste)

        self.generer()

    def tegnBrett(self):
        for x in range(self._kolonner):
            for i in range(self._rader):
                print(self._rutenett[x][i].hentStatusTegn(), end="")
            print("")
        print("\n"*10)

    def oppdatering(self):
        self._gNr += 1

    def finnAntallLevende(self):
        pass

    def generer(self):
        for x in self._rutenett:
            for i in x:
                rand = random.randint(0,2)
                if rand == 2:
                    i.settLevende()

    def finnNabo(self , x, y):
        naboeliste = []



brett = Spillebrett(10,10)
brett.tegnBrett()
