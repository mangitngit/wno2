import numpy as np
from colorama import *

init(wrap=False)

"""
[ Y X ]
"""

notacja = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7
}


class Kolory:
    niebieski = "niebieski"
    czerwony = "czerwony"
    puste_pole = " "


class Figura:
    znak = " "

    def __init__(self, pozycja, cz_b):
        self.y = pozycja[0]
        self.x = pozycja[1]
        self.ruchy = []
        self.bicie = []
        if cz_b:
            self.kolor = Kolory.niebieski
        else:
            self.kolor = Kolory.czerwony

    def mozliwe_ruchy(self, plansza):
        pass


class Pionek(Figura):
    znak = 'p'

    def __init__(self, pozycja, cz_b, pierwszy_ruch):
        Figura.__init__(self, pozycja, cz_b)
        self.pierwszy_ruch = pierwszy_ruch

    def mozliwe_ruchy(self, plansza):
        if self.kolor == Kolory.czerwony:
            if self.pierwszy_ruch:
                if plansza[self.y - 2, self.x].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y - 2, self.x])
                if plansza[self.y - 1, self.x].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y - 1, self.x])

                if self.x - 1 >= 0 and plansza[self.y - 1, self.x - 1].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y - 1, self.x - 1])
                    self.bicie.append([self.y - 1, self.x - 1])
                if self.x + 1 < 8 and plansza[self.y - 1, self.x + 1].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y - 1, self.x + 1])
                    self.bicie.append([self.y - 1, self.x + 1])
            else:
                if self.y - 1 >= 0 and plansza[self.y - 1, self.x].kolor == Kolory.puste_pole:  # przód
                    self.ruchy.append([self.y - 1, self.x])

                if self.x - 1 >= 0 and plansza[self.y - 1, self.x - 1].kolor == Kolory.niebieski:  # bicia
                    self.ruchy.append([self.y - 1, self.x - 1])
                    self.bicie.append([self.y - 1, self.x - 1])
                if self.x + 1 < 8 and plansza[self.y - 1, self.x + 1].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y - 1, self.x + 1])
                    self.bicie.append([self.y - 1, self.x + 1])
            return self.ruchy, self.bicie

        if self.kolor == Kolory.niebieski:
            if self.pierwszy_ruch:
                if plansza[self.y + 2, self.x].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y + 2, self.x])
                if plansza[self.y + 1, self.x].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y + 1, self.x])

                if self.x - 1 >= 0 and plansza[self.y + 1, self.x - 1].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y + 1, self.x - 1])
                    self.bicie.append([self.y + 1, self.x - 1])
                if self.x + 1 < 8 and plansza[self.y + 1, self.x + 1].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y + 1, self.x + 1])
                    self.bicie.append([self.y + 1, self.x + 1])
            else:
                if self.y + 1 < 8 and plansza[self.y + 1, self.x].kolor == Kolory.puste_pole:  # przód
                    self.ruchy.append([self.y + 1, self.x])

                if self.x - 1 >= 0 and plansza[self.y + 1, self.x - 1].kolor == Kolory.czerwony:  # bicia
                    self.ruchy.append([self.y + 1, self.x - 1])
                    self.bicie.append([self.y + 1, self.x - 1])
                if self.x + 1 < 8 and plansza[self.y + 1, self.x + 1].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y + 1, self.x + 1])
                    self.bicie.append([self.y + 1, self.x + 1])
            return self.ruchy, self.bicie


class Wieza(Figura):
    znak = 'w'

    def __init__(self, pozycja, cz_b, pierwszy_ruch):
        Figura.__init__(self, pozycja, cz_b)
        self.pierwszy_ruch = pierwszy_ruch

    def mozliwe_ruchy(self, plansza):
        if self.kolor == Kolory.czerwony:
            for i in range(self.x + 1, 8):  # w prawo
                if plansza[self.y, i].kolor == Kolory.czerwony:
                    break
                elif plansza[self.y, i].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y, i])
                    self.bicie.append([self.y, i])
                    break
                elif plansza[self.y, i].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y, i])

            for i in range(self.x - 1, -1, -1):  # w lewo
                if plansza[self.y, i].kolor == Kolory.czerwony:
                    break
                elif plansza[self.y, i].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y, i])
                    self.bicie.append([self.y, i])
                    break
                elif plansza[self.y, i].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y, i])

            for i in range(self.y + 1, 8):  # w prawo
                if plansza[i, self.x].kolor == Kolory.czerwony:
                    break
                elif plansza[i, self.x].kolor == Kolory.niebieski:
                    self.ruchy.append([i, self.x])
                    self.bicie.append([i, self.x])
                    break
                elif plansza[i, self.x].kolor == Kolory.puste_pole:
                    self.ruchy.append([i, self.x])

            for i in range(self.y - 1, -1, -1):  # w lewo
                if plansza[i, self.x].kolor == Kolory.czerwony:
                    break
                elif plansza[i, self.x].kolor == Kolory.niebieski:
                    self.ruchy.append([i, self.x])
                    self.bicie.append([i, self.x])
                    break
                elif plansza[i, self.x].kolor == Kolory.puste_pole:
                    self.ruchy.append([i, self.x])
            return self.ruchy, self.bicie

        if self.kolor == Kolory.niebieski:
            for i in range(self.x + 1, 8):  # w prawo
                if plansza[self.y, i].kolor == Kolory.niebieski:
                    break
                elif plansza[self.y, i].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y, i])
                    self.bicie.append([self.y, i])
                    break
                elif plansza[self.y, i].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y, i])

            for i in range(self.x - 1, -1, -1):  # w lewo
                if plansza[self.y, i].kolor == Kolory.niebieski:
                    break
                elif plansza[self.y, i].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y, i])
                    self.bicie.append([self.y, i])
                    break
                elif plansza[self.y, i].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y, i])

            for i in range(self.y + 1, 8):  # w prawo
                if plansza[i, self.x].kolor == Kolory.niebieski:
                    break
                elif plansza[i, self.x].kolor == Kolory.czerwony:
                    self.ruchy.append([i, self.x])
                    self.bicie.append([i, self.x])
                    break
                elif plansza[i, self.x].kolor == Kolory.puste_pole:
                    self.ruchy.append([i, self.x])

            for i in range(self.y - 1, -1, -1):  # w lewo
                if plansza[i, self.x].kolor == Kolory.niebieski:
                    break
                elif plansza[i, self.x].kolor == Kolory.czerwony:
                    self.ruchy.append([i, self.x])
                    self.bicie.append([i, self.x])
                    break
                elif plansza[i, self.x].kolor == Kolory.puste_pole:
                    self.ruchy.append([i, self.x])
            return self.ruchy, self.bicie


class Goniec(Figura):
    znak = 'g'

    def __init__(self, pozycja, cz_b):
        Figura.__init__(self, pozycja, cz_b)

    def mozliwe_ruchy(self, plansza):
        if self.kolor == Kolory.czerwony:
            buf = 1
            for i in range(self.x + 1, 8):  # po skosie w górę w prawo
                if self.y - buf < 0:
                    break
                if plansza[self.y - buf, i].kolor == Kolory.czerwony:
                    break
                elif plansza[self.y - buf, i].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y - buf, i])
                    self.bicie.append([self.y - buf, i])
                    break
                elif plansza[self.y - buf, i].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y - buf, i])
                buf += 1

            buf = 1
            for i in range(self.x - 1, -1, -1):  # po skosie w górę w lewo
                if self.y - buf < 0:
                    break
                if plansza[self.y - buf, i].kolor == Kolory.czerwony:
                    break
                elif plansza[self.y - buf, i].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y - buf, i])
                    self.bicie.append([self.y - buf, i])
                    break
                elif plansza[self.y - buf, i].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y - buf, i])
                buf += 1

            buf = 1
            for i in range(self.x + 1, 8):  # po skosie w dół w prawo
                if self.y + buf >= 8:
                    break
                if plansza[self.y + buf, i].kolor == Kolory.czerwony:
                    break
                elif plansza[self.y + buf, i].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y + buf, i])
                    self.bicie.append([self.y + buf, i])
                    break
                elif plansza[self.y + buf, i].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y + buf, i])
                buf += 1

            buf = 1
            for i in range(self.x - 1, -1, -1):  # po skosie w dół w lewo
                if self.y + buf >= 8:
                    break
                if plansza[self.y + buf, i].kolor == Kolory.czerwony:
                    break
                elif plansza[self.y + buf, i].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y + buf, i])
                    self.bicie.append([self.y + buf, i])
                    break
                elif plansza[self.y + buf, i].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y + buf, i])
                buf += 1
            return self.ruchy, self.bicie

        if self.kolor == Kolory.niebieski:
            buf = 1
            for i in range(self.x + 1, 8):  # po skosie w górę w prawo
                if self.y - buf < 0:
                    break
                if plansza[self.y - buf, i].kolor == Kolory.niebieski:
                    break
                elif plansza[self.y - buf, i].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y - buf, i])
                    self.bicie.append([self.y - buf, i])
                    break
                elif plansza[self.y - buf, i].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y - buf, i])
                buf += 1

            buf = 1
            for i in range(self.x - 1, -1, -1):  # po skosie w górę w lewo
                if self.y - buf < 0:
                    break
                if plansza[self.y - buf, i].kolor == Kolory.niebieski:
                    break
                elif plansza[self.y - buf, i].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y - buf, i])
                    self.bicie.append([self.y - buf, i])
                    break
                elif plansza[self.y - buf, i].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y - buf, i])
                buf += 1

            buf = 1
            for i in range(self.x + 1, 8):  # po skosie w dół w prawo
                if self.y + buf >= 8:
                    break
                if plansza[self.y + buf, i].kolor == Kolory.niebieski:
                    break
                elif plansza[self.y + buf, i].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y + buf, i])
                    self.bicie.append([self.y + buf, i])
                    break
                elif plansza[self.y + buf, i].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y + buf, i])
                buf += 1

            buf = 1
            for i in range(self.x - 1, -1, -1):  # po skosie w dół w lewo
                if self.y + buf >= 8:
                    break
                if plansza[self.y + buf, i].kolor == Kolory.niebieski:
                    break
                elif plansza[self.y + buf, i].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y + buf, i])
                    self.bicie.append([self.y + buf, i])
                    break
                elif plansza[self.y + buf, i].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y + buf, i])
                buf += 1
            return self.ruchy, self.bicie


class Skoczek(Figura):
    znak = 's'

    def __init__(self, pozycja, cz_b):
        Figura.__init__(self, pozycja, cz_b)

    def mozliwe_ruchy(self, plansza):
        if self.kolor == Kolory.czerwony:
            if self.y - 2 >= 0:  # na gorze
                if self.x - 1 >= 0 and plansza[self.y - 2, self.x - 1].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y - 2, self.x - 1])
                    self.bicie.append([self.y - 2, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y - 2, self.x - 1].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y - 2, self.x - 1])

                if self.x + 1 < 8 and plansza[self.y - 2, self.x + 1].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y - 2, self.x + 1])
                    self.bicie.append([self.y - 2, self.x + 1])
                elif self.x + 1 < 8 and plansza[self.y - 2, self.x + 1].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y - 2, self.x + 1])

            if self.y + 2 < 8:  # na dole
                if self.x - 1 >= 0 and plansza[self.y + 2, self.x - 1].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y + 2, self.x - 1])
                    self.bicie.append([self.y + 2, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y + 2, self.x - 1].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y + 2, self.x - 1])

                if self.x + 1 < 8 and plansza[self.y + 2, self.x + 1].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y + 2, self.x + 1])
                    self.bicie.append([self.y + 2, self.x + 1])
                elif self.x + 1 < 8 and plansza[self.y + 2, self.x + 1].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y + 2, self.x + 1])

            if self.x - 2 >= 0:  # po lewej
                if self.y - 1 >= 0 and plansza[self.y - 1, self.x - 2].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y - 1, self.x - 2])
                    self.bicie.append([self.y - 1, self.x - 2])
                elif self.y - 1 >= 0 and plansza[self.y - 1, self.x - 2].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y - 1, self.x - 2])

                if self.y + 1 < 8 and plansza[self.y + 1, self.x - 2].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y + 1, self.x - 2])
                    self.bicie.append([self.y + 1, self.x - 2])
                elif self.y + 1 < 8 and plansza[self.y + 1, self.x - 2].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y + 1, self.x - 2])

            if self.x + 2 < 8:  # po prawej
                if self.y - 1 >= 0 and plansza[self.y - 1, self.x + 2].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y - 1, self.x + 2])
                    self.bicie.append([self.y - 1, self.x + 2])
                elif self.y - 1 >= 0 and plansza[self.y - 1, self.x + 2].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y - 1, self.x + 2])

                if self.y + 1 < 8 and plansza[self.y + 1, self.x + 2].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y + 1, self.x + 2])
                    self.bicie.append([self.y + 1, self.x + 2])
                elif self.y + 1 < 8 and plansza[self.y + 1, self.x + 2].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y + 1, self.x + 2])
            return self.ruchy, self.bicie

        if self.kolor == Kolory.niebieski:
            if self.y - 2 >= 0:  # na gorze
                if self.x - 1 >= 0 and plansza[self.y - 2, self.x - 1].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y - 2, self.x - 1])
                    self.bicie.append([self.y - 2, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y - 2, self.x - 1].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y - 2, self.x - 1])

                if self.x + 1 < 8 and plansza[self.y - 2, self.x + 1].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y - 2, self.x + 1])
                    self.bicie.append([self.y - 2, self.x + 1])
                elif self.x + 1 < 8 and plansza[self.y - 2, self.x + 1].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y - 2, self.x + 1])

            if self.y + 2 < 8:  # na dole
                if self.x - 1 >= 0 and plansza[self.y + 2, self.x - 1].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y + 2, self.x - 1])
                    self.bicie.append([self.y + 2, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y + 2, self.x - 1].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y + 2, self.x - 1])

                if self.x + 1 < 8 and plansza[self.y + 2, self.x + 1].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y + 2, self.x + 1])
                    self.bicie.append([self.y + 2, self.x + 1])
                elif self.x + 1 < 8 and plansza[self.y + 2, self.x + 1].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y + 2, self.x + 1])

            if self.x - 2 >= 0:  # po lewej
                if self.y - 1 >= 0 and plansza[self.y - 1, self.x - 2].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y - 1, self.x - 2])
                    self.bicie.append([self.y - 1, self.x - 2])
                elif self.y - 1 >= 0 and plansza[self.y - 1, self.x - 2].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y - 1, self.x - 2])

                if self.y + 1 < 8 and plansza[self.y + 1, self.x - 2].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y + 1, self.x - 2])
                    self.bicie.append([self.y + 1, self.x - 2])
                elif self.y + 1 < 8 and plansza[self.y + 1, self.x - 2].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y + 1, self.x - 2])

            if self.x + 2 < 8:  # po prawej
                if self.y - 1 >= 0 and plansza[self.y - 1, self.x + 2].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y - 1, self.x + 2])
                    self.bicie.append([self.y - 1, self.x + 2])
                elif self.y - 1 >= 0 and plansza[self.y - 1, self.x + 2].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y - 1, self.x + 2])

                if self.y + 1 < 8 and plansza[self.y + 1, self.x + 2].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y + 1, self.x + 2])
                    self.bicie.append([self.y + 1, self.x + 2])
                elif self.y + 1 < 8 and plansza[self.y + 1, self.x + 2].kolor == Kolory.puste_pole:
                    self.ruchy.append([self.y + 1, self.x + 2])
            return self.ruchy, self.bicie


class Krol(Figura):
    znak = 'k'
    atakowany = False

    def __init__(self, pozycja, cz_b, pierwszy_ruch):
        Figura.__init__(self, pozycja, cz_b)
        self.pierwszy_ruch = pierwszy_ruch

    def mozliwe_ruchy(self, plansza):
        if self.kolor == Kolory.czerwony:
            if self.y - 1 >= 0 and plansza[self.y - 1, self.x].kolor == Kolory.puste_pole:  # gora
                self.ruchy.append([self.y - 1, self.x])
            elif self.y - 1 >= 0 and plansza[self.y - 1, self.x].kolor == Kolory.niebieski:
                self.ruchy.append([self.y - 1, self.x])
                self.bicie.append([self.y - 1, self.x])

            if self.y + 1 < 8 and plansza[self.y + 1, self.x].kolor == Kolory.puste_pole:  # dol
                self.ruchy.append([self.y + 1, self.x])
            elif self.y + 1 < 8 and plansza[self.y + 1, self.x].kolor == Kolory.niebieski:
                self.ruchy.append([self.y + 1, self.x])
                self.bicie.append([self.y + 1, self.x])

            if self.x - 1 >= 0 and plansza[self.y, self.x - 1].kolor == Kolory.puste_pole:  # lewo
                self.ruchy.append([self.y, self.x - 1])
            elif self.x - 1 >= 0 and plansza[self.y, self.x - 1].kolor == Kolory.niebieski:
                self.ruchy.append([self.y, self.x - 1])
                self.bicie.append([self.y, self.x - 1])

            if self.x + 1 < 8 and plansza[self.y, self.x + 1].kolor == Kolory.puste_pole:  # prawo
                self.ruchy.append([self.y, self.x + 1])
            elif self.x + 1 < 8 and plansza[self.y, self.x + 1].kolor == Kolory.niebieski:
                self.ruchy.append([self.y, self.x + 1])
                self.bicie.append([self.y, self.x + 1])

            if self.y - 1 >= 0:
                if self.x - 1 >= 0 and plansza[self.y - 1, self.x - 1].kolor == Kolory.puste_pole:  # gora lewo
                    self.ruchy.append([self.y - 1, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y - 1, self.x - 1].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y - 1, self.x - 1])
                    self.bicie.append([self.y - 1, self.x - 1])

                if self.x + 1 >= 0 and plansza[self.y - 1, self.x + 1].kolor == Kolory.puste_pole:  # gora prawo
                    self.ruchy.append([self.y - 1, self.x + 1])
                elif self.x + 1 >= 0 and plansza[self.y - 1, self.x + 1].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y - 1, self.x + 1])
                    self.bicie.append([self.y - 1, self.x + 1])

            if self.y + 1 < 8:
                if self.x - 1 >= 0 and plansza[self.y + 1, self.x - 1].kolor == Kolory.puste_pole:  # dół lewo
                    self.ruchy.append([self.y + 1, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y + 1, self.x - 1].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y + 1, self.x - 1])
                    self.bicie.append([self.y + 1, self.x - 1])

                if self.x + 1 >= 0 and plansza[self.y + 1, self.x + 1].kolor == Kolory.puste_pole:  # dół prawo
                    self.ruchy.append([self.y + 1, self.x + 1])
                elif self.x + 1 >= 0 and plansza[self.y + 1, self.x + 1].kolor == Kolory.niebieski:
                    self.ruchy.append([self.y + 1, self.x + 1])
                    self.bicie.append([self.y + 1, self.x + 1])

            if self.pierwszy_ruch and plansza[self.y, self.x + 3].znak == Wieza.znak:
                if plansza[self.y, self.x + 3].pierwszy_ruch:
                    if plansza[self.y, self.x + 1].znak == Kolory.puste_pole and plansza[self.y, self.x + 2].znak == \
                            Kolory.puste_pole:
                        self.ruchy.append([self.y, self.x + 2])

            if self.pierwszy_ruch and plansza[self.y, self.x - 4].znak == Wieza.znak:
                if plansza[self.y, self.x - 4].pierwszy_ruch:
                    if plansza[self.y, self.x - 1].znak == Kolory.puste_pole and plansza[
                        self.y, self.x - 2].znak == Kolory.puste_pole and plansza[self.y, self.x - 3].znak == \
                            Kolory.puste_pole:
                        self.ruchy.append([self.y, self.x - 2])

            return self.ruchy, self.bicie

        if self.kolor == Kolory.niebieski:
            if self.y - 1 >= 0 and plansza[self.y - 1, self.x].kolor == Kolory.puste_pole:  # gora
                self.ruchy.append([self.y - 1, self.x])
            elif self.y - 1 >= 0 and plansza[self.y - 1, self.x].kolor == Kolory.czerwony:
                self.ruchy.append([self.y - 1, self.x])
                self.bicie.append([self.y - 1, self.x])

            if self.y + 1 < 8 and plansza[self.y + 1, self.x].kolor == Kolory.puste_pole:  # dol
                self.ruchy.append([self.y + 1, self.x])
            elif self.y + 1 < 8 and plansza[self.y + 1, self.x].kolor == Kolory.czerwony:
                self.ruchy.append([self.y + 1, self.x])
                self.bicie.append([self.y + 1, self.x])

            if self.x - 1 >= 0 and plansza[self.y, self.x - 1].kolor == Kolory.puste_pole:  # lewo
                self.ruchy.append([self.y, self.x - 1])
            elif self.x - 1 >= 0 and plansza[self.y, self.x - 1].kolor == Kolory.czerwony:
                self.ruchy.append([self.y, self.x - 1])
                self.bicie.append([self.y, self.x - 1])

            if self.x + 1 < 8 and plansza[self.y, self.x + 1].kolor == Kolory.puste_pole:  # prawo
                self.ruchy.append([self.y, self.x + 1])
            elif self.x + 1 < 8 and plansza[self.y, self.x + 1].kolor == Kolory.czerwony:
                self.ruchy.append([self.y, self.x + 1])
                self.bicie.append([self.y, self.x + 1])

            if self.y - 1 >= 0:
                if self.x - 1 >= 0 and plansza[self.y - 1, self.x - 1].kolor == Kolory.puste_pole:  # gora lewo
                    self.ruchy.append([self.y - 1, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y - 1, self.x - 1].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y - 1, self.x - 1])
                    self.bicie.append([self.y - 1, self.x - 1])

                if self.x + 1 >= 0 and plansza[self.y - 1, self.x + 1].kolor == Kolory.puste_pole:  # gora prawo
                    self.ruchy.append([self.y - 1, self.x + 1])
                elif self.x + 1 >= 0 and plansza[self.y - 1, self.x + 1].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y - 1, self.x + 1])
                    self.bicie.append([self.y - 1, self.x + 1])

            if self.y + 1 < 8:
                if self.x - 1 >= 0 and plansza[self.y + 1, self.x - 1].kolor == Kolory.puste_pole:  # dół lewo
                    self.ruchy.append([self.y + 1, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y + 1, self.x - 1].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y + 1, self.x - 1])
                    self.bicie.append([self.y + 1, self.x - 1])

                if self.x + 1 >= 0 and plansza[self.y + 1, self.x + 1].kolor == Kolory.puste_pole:  # dół prawo
                    self.ruchy.append([self.y + 1, self.x + 1])
                elif self.x + 1 >= 0 and plansza[self.y + 1, self.x + 1].kolor == Kolory.czerwony:
                    self.ruchy.append([self.y + 1, self.x + 1])
                    self.bicie.append([self.y + 1, self.x + 1])

            if self.pierwszy_ruch and plansza[self.y, self.x + 3].znak == Wieza.znak:
                if plansza[self.y, self.x + 3].pierwszy_ruch:
                    if plansza[self.y, self.x + 1].znak == Kolory.puste_pole and plansza[self.y, self.x + 2].znak == \
                            Kolory.puste_pole:
                        self.ruchy.append([self.y, self.x + 2])

            if self.pierwszy_ruch and plansza[self.y, self.x - 4].znak == Wieza.znak:
                if plansza[self.y, self.x - 4].pierwszy_ruch:
                    if plansza[self.y, self.x - 1].znak == Kolory.puste_pole and plansza[
                        self.y, self.x - 2].znak == Kolory.puste_pole and plansza[self.y, self.x - 3].znak == \
                            Kolory.puste_pole:
                        self.ruchy.append([self.y, self.x - 2])

            return self.ruchy, self.bicie


class Hetman(Goniec, Wieza):
    znak = 'h'

    def __init__(self, pozycja, cz_b):
        Figura.__init__(self, pozycja, cz_b)

    def mozliwe_ruchy(self, plansza):
        Goniec.mozliwe_ruchy(self, plansza)
        Wieza.mozliwe_ruchy(self, plansza)

        return self.ruchy, self.bicie


class Pole:
    znak = " "
    kolor = " "

    @staticmethod
    def mozliwe_ruchy(_):
        return [], []


class Plansza:
    wygrana = True
    czer_nieb_ruch = True
    krol_niebieski = Krol([0, 4], True, True)
    krol_czerwony = Krol([7, 4], False, True)

    def __init__(self):
        self.mozliwe_ruchy_biezacego_pionka = []
        self.mozliwe_bicie_biezacego_pionka = []
        self.wszystkie_ruchy = []
        self.wszystkie_bicia = []
        self.ruchy_niebieskich = []
        self.ruchy_czerwonych = []

        self.plansza = np.empty((9, 9), dtype=object)
        self.plansza[:] = Pole()
        self.plansza[8, :] = ' A', ' B', ' C', ' D', ' E', ' F', ' G', ' H', ' .'
        for i in range(8):
            self.plansza[i, 8] = ' ' + str(i + 1)

    def rysuj(self, polecenie):
        for y in range(8):
            for x in range(8):
                flaga1 = [i for i in self.mozliwe_bicie_biezacego_pionka if i == [y, x]]
                flaga2 = [i for i in self.mozliwe_ruchy_biezacego_pionka if i == [y, x]]
                symbol = self.plansza[y, x].znak
                if self.plansza[y, x].kolor == Kolory.czerwony:
                    symbol = Fore.RED + symbol
                if self.plansza[y, x].kolor == Kolory.niebieski:
                    symbol = Fore.BLUE + symbol
                if [x, y] == [int(polecenie[0]), int(polecenie[1])]:
                    print(Back.LIGHTGREEN_EX + '\033[1m' + ' ' + Back.LIGHTGREEN_EX + symbol + ' \033[30m', end="")
                elif flaga1:
                    print(Back.LIGHTBLUE_EX + '\033[1m' + ' ' + Back.LIGHTBLUE_EX + symbol + ' \033[30m', end="")
                elif flaga2:
                    print(Back.LIGHTYELLOW_EX + '\033[1m' + ' ' + Back.LIGHTYELLOW_EX + symbol + ' \033[30m', end="")
                elif (x + y) % 2 == 1:
                    print(Back.LIGHTWHITE_EX + '\033[1m' + ' ' + Back.LIGHTWHITE_EX + symbol + ' \033[30m', end="")
                else:
                    print(Back.LIGHTBLACK_EX + '\033[1m' + ' ' + Back.LIGHTBLACK_EX + symbol + ' \033[30m', end="")

                self.plansza[y, x].ruchy = []
                self.plansza[y, x].bicie = []
            print(self.plansza[y, 8])
        for i in self.plansza[8, :]:
            print(i, end=' ')
        print()

    def pionki(self):
        # niebieskie
        for i in range(8):
            self.plansza[1, i] = Pionek([1, i], True, True)
        self.plansza[0, 0] = Wieza([0, 0], True, True)
        self.plansza[0, 7] = Wieza([0, 7], True, True)
        self.plansza[0, 1] = Skoczek([0, 1], True)
        self.plansza[0, 6] = Skoczek([0, 6], True)
        self.plansza[0, 2] = Goniec([0, 2], True)
        self.plansza[0, 5] = Goniec([0, 5], True)
        self.plansza[0, 3] = Hetman([0, 3], True)
        self.plansza[0, 4] = self.krol_niebieski

        # czerwone
        for i in range(8):
            self.plansza[6, i] = Pionek([6, i], False, True)
        self.plansza[7, 0] = Wieza([7, 0], False, True)
        self.plansza[7, 7] = Wieza([7, 7], False, True)
        self.plansza[7, 1] = Skoczek([7, 1], False)
        self.plansza[7, 6] = Skoczek([7, 6], False)
        self.plansza[7, 2] = Goniec([7, 2], False)
        self.plansza[7, 5] = Goniec([7, 5], False)
        self.plansza[7, 3] = Hetman([7, 3], False)
        self.plansza[7, 4] = self.krol_czerwony

    def mozliwe_ruchy_wszystkich(self):
        self.wszystkie_bicia = []
        self.wszystkie_ruchy = []
        for y in range(8):
            for x in range(8):
                ruch, bicie = self.plansza[y, x].mozliwe_ruchy(self.plansza)
                self.wszystkie_bicia.append(bicie)
                self.wszystkie_ruchy.append(ruch)
                if self.plansza[y, x].kolor == Kolory.niebieski:
                    self.ruchy_niebieskich.append(ruch)
                if self.plansza[y, x].kolor == Kolory.czerwony:
                    self.ruchy_czerwonych.append(ruch)

        buf_wszystkich = []
        for x in self.wszystkie_bicia:
            for y in x:
                buf_wszystkich.append(y)
        self.krol_czerwony.atakowany = [i for i in buf_wszystkich if i == [self.krol_czerwony.y, self.krol_czerwony.x]]
        self.krol_niebieski.atakowany = [i for i in buf_wszystkich if
                                         i == [self.krol_niebieski.y, self.krol_niebieski.x]]

        self.szach()

    def pole(self, x, y):
        self.mozliwe_ruchy_biezacego_pionka = self.plansza[y, x].ruchy
        self.mozliwe_bicie_biezacego_pionka = self.plansza[y, x].bicie

    def ruch(self, x, y, x_docelowe, y_docelowe):
        flaga = [i for i in self.mozliwe_ruchy_biezacego_pionka if i == [y_docelowe, x_docelowe]]
        self.mozliwe_ruchy_biezacego_pionka = []
        self.mozliwe_bicie_biezacego_pionka = []

        if flaga and self.czer_nieb_ruch:  # ruch czerwonych
            if self.plansza[y, x].znak == 'p' or 'w' or 'k':
                self.plansza[y, x].pierwszy_ruch = False
            if self.plansza[y, x].znak == 'p' and y == 1:
                self.plansza[y, x] = Hetman([y, x], True)

            if self.plansza[y, x].znak == 'k' and x_docelowe - x == 2:  # roszada po prawej
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole()
                self.plansza[y, x + 1] = self.plansza[y, x + 3]
                self.plansza[y, x + 3] = Pole()
            elif self.plansza[y, x].znak == 'k' and x_docelowe - x == -2:
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole()
                self.plansza[y, x - 1] = self.plansza[y, x - 4]
                self.plansza[y, x - 4] = Pole()
            elif self.plansza[y_docelowe, x_docelowe].kolor == Kolory.niebieski:  # bicie
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole()
            else:
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]  # ruch
                self.plansza[y, x] = Pole()

            self.plansza[y_docelowe, x_docelowe].x = x_docelowe
            self.plansza[y_docelowe, x_docelowe].y = y_docelowe

            self.czer_nieb_ruch = not self.czer_nieb_ruch

        elif flaga and not self.czer_nieb_ruch:  # ruch niebieskich
            if self.plansza[y, x].znak == 'p' or 'w' or 'k':
                self.plansza[y, x].pierwszy_ruch = False
            if self.plansza[y, x].znak == 'p' and y == 6:
                self.plansza[y, x] = Hetman([y, x], True)

            if self.plansza[y, x].znak == 'k' and x_docelowe - x == 2:  # roszada po prawej
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole()
                self.plansza[y, x + 1] = self.plansza[y, x + 3]
                self.plansza[y, x + 3] = Pole()
            elif self.plansza[y_docelowe, x_docelowe].kolor == Kolory.czerwony:
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole()
            else:
                bufor = self.plansza[y_docelowe, x_docelowe]
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = bufor

            self.plansza[y_docelowe, x_docelowe].x = x_docelowe
            self.plansza[y_docelowe, x_docelowe].y = y_docelowe

            self.czer_nieb_ruch = not self.czer_nieb_ruch

    def szach(self):
        if self.krol_czerwony.atakowany:  # or self.krol_niebieski.atakowany:
            print("SZACH", end=' ')

            buf_niebieskich = []
            for x in self.ruchy_niebieskich:
                for y in x:
                    buf_niebieskich.append(y)
            flaga1 = False
            for ruch in self.krol_czerwony.ruchy:
                flaga2 = [i for i in buf_niebieskich if i == ruch]
                if not flaga2:
                    flaga1 = True
            if not flaga1:
                print("MAT - wygrana niebieskich")
                self.wygrana = False
            else:
                print()
        if self.krol_niebieski.atakowany:  # or self.krol_niebieski.atakowany:
            print("SZACH", end=' ')

            buf_czerwonych = []
            for x in self.ruchy_czerwonych:
                for y in x:
                    buf_czerwonych.append(y)
            flaga1 = False
            for ruch in self.krol_niebieski.ruchy:
                flaga2 = [i for i in buf_czerwonych if i == ruch]
                if not flaga2:
                    flaga1 = True
            if not flaga1:
                print("MAT - wygrana czerwonych")
                self.wygrana = False
            else:
                print()


def main():
    szachy = Plansza()
    szachy.pionki()

    while szachy.wygrana:
        print("=" * 25)
        szachy.rysuj([10, 10])
        szachy.mozliwe_ruchy_wszystkich()

        if not szachy.wygrana:
            break

        if szachy.czer_nieb_ruch:
            print(Fore.RED + "Ruch czerwonych\033[30m")
        else:
            print(Fore.BLUE + "Ruch niebieskich\033[30m")

        try:
            polecenie_1 = input("Podaj pole: ")

            szachy.pole(notacja[polecenie_1[0]], int(polecenie_1[1]) - 1)
            szachy.rysuj([notacja[polecenie_1[0]], int(polecenie_1[1]) - 1])
            try:
                polecenie_2 = input("Podaj ruch pionka: ")

                szachy.ruch(notacja[polecenie_1[0]], int(polecenie_1[1]) - 1,
                            notacja[polecenie_2[0]], int(polecenie_2[1]) - 1)

            except:
                szachy.mozliwe_bicie_biezacego_pionka = []
                szachy.mozliwe_ruchy_biezacego_pionka = []
                print("Nieprawidlowy ruch")
                pass
        except:
            print("Nieprawidlowe pole")
            pass


if __name__ == "__main__":
    main()
