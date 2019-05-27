import numpy as np
from colorama import *
init(wrap=False)

"""
[ Y X ]
"""
wygrana = True
figura_niebieska = "\033[34m"
figura_czerwona = "\033[31m"
puste_pole = ""
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


class Figura:
    znak = ""

    def __init__(self, pozycja, cz_b):
        self.y = pozycja[0]
        self.x = pozycja[1]
        self.ruchy = []
        if cz_b:
            self.znak = Fore.BLUE+self.znak
        else:
            self.znak = Fore.RED+self.znak

    def mozliwe_ruchy(self, plansza):
        pass


class Pionek(Figura):
    znak = 'p'

    def __init__(self, pozycja, cz_b, pierwszy_ruch):
        Figura.__init__(self, pozycja, cz_b)
        self.pierwszy_ruch = pierwszy_ruch

    def mozliwe_ruchy(self, plansza):
        if self.znak[:-1] == figura_czerwona:
            if self.pierwszy_ruch:
                if plansza[self.y - 2, self.x].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - 2, self.x])
                if plansza[self.y - 1, self.x].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - 1, self.x])

                if self.x-1 >= 0 and plansza[self.y - 1, self.x - 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y - 1, self.x - 1])
                if self.x+1 < 8 and plansza[self.y - 1, self.x + 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y - 1, self.x + 1])
            else:
                if self.y-1 >= 0 and plansza[self.y - 1, self.x].znak[:-1] == puste_pole:            # przód
                    self.ruchy.append([self.y - 1, self.x])

                if self.x-1 >= 0 and plansza[self.y - 1, self.x - 1].znak[:-1] == figura_niebieska:   # bicia
                    self.ruchy.append([self.y - 1, self.x - 1])
                if self.x+1 < 8 and plansza[self.y - 1, self.x + 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y - 1, self.x + 1])

        if self.znak[:-1] == figura_niebieska:
            if self.pierwszy_ruch:
                if plansza[self.y + 2, self.x].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 2, self.x])
                if plansza[self.y + 1, self.x].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 1, self.x])

                if self.x-1 >= 0 and plansza[self.y + 1, self.x - 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + 1, self.x - 1])
                if self.x+1 < 8 and plansza[self.y + 1, self.x + 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + 1, self.x + 1])
            else:
                if self.y+1 < 8 and plansza[self.y + 1, self.x].znak[:-1] == puste_pole:            # przód
                    self.ruchy.append([self.y + 1, self.x])

                if self.x-1 >= 0 and plansza[self.y + 1, self.x - 1].znak[:-1] == figura_czerwona:   # bicia
                    self.ruchy.append([self.y + 1, self.x - 1])
                if self.x+1 < 8 and plansza[self.y + 1, self.x + 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + 1, self.x + 1])
        return self.ruchy


class Wieza(Figura):
    znak = 'w'

    def __init__(self, pozycja, cz_b):
        Figura.__init__(self, pozycja, cz_b)

    def mozliwe_ruchy(self, plansza):
        if self.znak[:-1] == figura_czerwona:
            for i in range(self.x + 1, 8):                          # w prawo
                if plansza[self.y, i].znak[:-1] == figura_czerwona:
                    break
                elif plansza[self.y, i].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y, i])
                    break
                elif plansza[self.y, i].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y, i])

            for i in range(self.x - 1, -1, -1):                          # w lewo
                if plansza[self.y, i].znak[:-1] == figura_czerwona:
                    break
                elif plansza[self.y, i].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y, i])
                    break
                elif plansza[self.y, i].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y, i])

            for i in range(self.y + 1, 8):                          # w prawo
                if plansza[i, self.x].znak[:-1] == figura_czerwona:
                    break
                elif plansza[i, self.x].znak[:-1] == figura_niebieska:
                    self.ruchy.append([i, self.x])
                    break
                elif plansza[i, self.x].znak[:-1] == puste_pole:
                    self.ruchy.append([i, self.x])

            for i in range(self.y - 1, -1, -1):                          # w lewo
                if plansza[i, self.x].znak[:-1] == figura_czerwona:
                    break
                elif plansza[i, self.x].znak[:-1] == figura_niebieska:
                    self.ruchy.append([i, self.x])
                    break
                elif plansza[i, self.x].znak[:-1] == puste_pole:
                    self.ruchy.append([i, self.x])

        if self.znak[:-1] == figura_niebieska:
            for i in range(self.x + 1, 8):                          # w prawo
                if plansza[self.y, i].znak[:-1] == figura_niebieska:
                    break
                elif plansza[self.y, i].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y, i])
                    break
                elif plansza[self.y, i].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y, i])

            for i in range(self.x - 1, -1, -1):                          # w lewo
                if plansza[self.y, i].znak[:-1] == figura_niebieska:
                    break
                elif plansza[self.y, i].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y, i])
                    break
                elif plansza[self.y, i].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y, i])

            for i in range(self.y + 1, 8):                          # w prawo
                if plansza[i, self.x].znak[:-1] == figura_niebieska:
                    break
                elif plansza[i, self.x].znak[:-1] == figura_czerwona:
                    self.ruchy.append([i, self.x])
                    break
                elif plansza[i, self.x].znak[:-1] == puste_pole:
                    self.ruchy.append([i, self.x])

            for i in range(self.y - 1, -1, -1):                          # w lewo
                if plansza[i, self.x].znak[:-1] == figura_niebieska:
                    break
                elif plansza[i, self.x].znak[:-1] == figura_czerwona:
                    self.ruchy.append([i, self.x])
                    break
                elif plansza[i, self.x].znak[:-1] == puste_pole:
                    self.ruchy.append([i, self.x])
        return self.ruchy


class Goniec(Figura):
    znak = 'g'

    def __init__(self, pozycja, cz_b):
        Figura.__init__(self, pozycja, cz_b)

    def mozliwe_ruchy(self, plansza):
        if self.znak[:-1] == figura_czerwona:
            buf = 1
            for i in range(self.x + 1, 8):                          # po skosie w górę w prawo
                if self.y - buf < 0:
                    break
                if plansza[self.y-buf, i].znak[:-1] == figura_czerwona:
                    break
                elif plansza[self.y-buf, i].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y - buf, i])
                    break
                elif plansza[self.y - buf, i].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - buf, i])
                buf += 1

            buf = 1
            for i in range(self.x - 1, -1, -1):                           # po skosie w górę w lewo
                if self.y - buf < 0:
                    break
                if plansza[self.y - buf, i].znak[:-1] == figura_czerwona:
                    break
                elif plansza[self.y - buf, i].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y - buf, i])
                    break
                elif plansza[self.y - buf, i].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - buf, i])
                buf += 1

            buf = 1
            for i in range(self.x + 1, 8):                                 # po skosie w dół w prawo
                if self.y + buf >= 8:
                    break
                if plansza[self.y + buf, i].znak[:-1] == figura_czerwona:
                    break
                elif plansza[self.y + buf, i].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y + buf, i])
                    break
                elif plansza[self.y + buf, i].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + buf, i])
                buf += 1

            buf = 1
            for i in range(self.x - 1, -1, -1):                            # po skosie w dół w lewo
                if self.y + buf >= 8:
                    break
                if plansza[self.y + buf, i].znak[:-1] == figura_czerwona:
                    break
                elif plansza[self.y + buf, i].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + buf, i])
                    break
                elif plansza[self.y + buf, i].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + buf, i])
                buf += 1

        if self.znak[:-1] == figura_niebieska:
            buf = 1
            for i in range(self.x + 1, 8):  # po skosie w górę w prawo
                if self.y - buf < 0:
                    break
                if plansza[self.y - buf, i].znak[:-1] == figura_niebieska:
                    break
                elif plansza[self.y - buf, i].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y - buf, i])
                    break
                elif plansza[self.y - buf, i].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - buf, i])
                buf += 1

            buf = 1
            for i in range(self.x - 1, -1, -1):  # po skosie w górę w lewo
                if self.y - buf < 0:
                    break
                if plansza[self.y - buf, i].znak[:-1] == figura_niebieska:
                    break
                elif plansza[self.y - buf, i].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y - buf, i])
                    break
                elif plansza[self.y - buf, i].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - buf, i])
                buf += 1

            buf = 1
            for i in range(self.x + 1, 8):  # po skosie w dół w prawo
                if self.y + buf >= 8:
                    break
                if plansza[self.y + buf, i].znak[:-1] == figura_niebieska:
                    break
                elif plansza[self.y + buf, i].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + buf, i])
                    break
                elif plansza[self.y + buf, i].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + buf, i])
                buf += 1

            buf = 1
            for i in range(self.x - 1, -1, -1):  # po skosie w dół w lewo
                if self.y + buf >= 8:
                    break
                if plansza[self.y + buf, i].znak[:-1] == figura_niebieska:
                    break
                elif plansza[self.y + buf, i].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + buf, i])
                    break
                elif plansza[self.y + buf, i].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + buf, i])
                buf += 1
        return self.ruchy


class Skoczek(Figura):
    znak = 's'

    def __init__(self, pozycja, cz_b):
        Figura.__init__(self, pozycja, cz_b)

    def mozliwe_ruchy(self, plansza):
        if self.znak[:-1] == figura_czerwona:
            if self.y - 2 >= 0:                             # na gorze
                if self.x - 1 >= 0 and plansza[self.y - 2, self.x - 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y - 2, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y - 2, self.x - 1].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - 2, self.x - 1])

                if self.x + 1 < 8 and plansza[self.y - 2, self.x + 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y - 2, self.x + 1])
                elif self.x + 1 < 8 and plansza[self.y - 2, self.x + 1].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - 2, self.x + 1])

            if self.y + 2 < 8:                             # na dole
                if self.x - 1 >= 0 and plansza[self.y + 2, self.x - 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y + 2, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y + 2, self.x - 1].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 2, self.x - 1])

                if self.x + 1 < 8 and plansza[self.y + 2, self.x + 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y + 2, self.x + 1])
                elif self.x + 1 < 8 and plansza[self.y + 2, self.x + 1].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 2, self.x + 1])

            if self.x - 2 >= 0:                             # po lewej
                if self.y - 1 >= 0 and plansza[self.y - 1, self.x - 2].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y - 1, self.x - 2])
                elif self.y - 1 >= 0 and plansza[self.y - 1, self.x - 2].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - 1, self.x - 2])

                if self.y + 1 < 8 and plansza[self.y + 1, self.x - 2].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y + 1, self.x - 2])
                elif self.y + 1 < 8 and plansza[self.y + 1, self.x - 2].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 1, self.x - 2])

            if self.x + 2 < 8:                             # po prawej
                if self.y - 1 >= 0 and plansza[self.y - 1, self.x + 2].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y - 1, self.x + 2])
                elif self.y - 1 >= 0 and plansza[self.y - 1, self.x + 2].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - 1, self.x + 2])

                if self.y + 1 < 8 and plansza[self.y + 1, self.x + 2].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y + 1, self.x + 2])
                elif self.y + 1 < 8 and plansza[self.y + 1, self.x + 2].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 1, self.x + 2])

        if self.znak[:-1] == figura_niebieska:
            if self.y - 2 >= 0:                             # na gorze
                if self.x - 1 >= 0 and plansza[self.y - 2, self.x - 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y - 2, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y - 2, self.x - 1].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - 2, self.x - 1])

                if self.x + 1 < 8 and plansza[self.y - 2, self.x + 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y - 2, self.x + 1])
                elif self.x + 1 < 8 and plansza[self.y - 2, self.x + 1].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - 2, self.x + 1])

            if self.y + 2 < 8:                             # na dole
                if self.x - 1 >= 0 and plansza[self.y + 2, self.x - 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + 2, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y + 2, self.x - 1].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 2, self.x - 1])

                if self.x + 1 < 8 and plansza[self.y + 2, self.x + 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + 2, self.x + 1])
                elif self.x + 1 < 8 and plansza[self.y + 2, self.x + 1].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 2, self.x + 1])

            if self.x - 2 >= 0:                             # po lewej
                if self.y - 1 >= 0 and plansza[self.y - 1, self.x - 2].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y - 1, self.x - 2])
                elif self.y - 1 >= 0 and plansza[self.y - 1, self.x - 2].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - 1, self.x - 2])

                if self.y + 1 < 8 and plansza[self.y + 1, self.x - 2].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + 1, self.x - 2])
                elif self.y + 1 < 8 and plansza[self.y + 1, self.x - 2].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 1, self.x - 2])

            if self.x + 2 < 8:                             # po prawej
                if self.y - 1 >= 0 and plansza[self.y - 1, self.x + 2].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y - 1, self.x + 2])
                elif self.y - 1 >= 0 and plansza[self.y - 1, self.x + 2].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - 1, self.x + 2])

                if self.y + 1 < 8 and plansza[self.y + 1, self.x + 2].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + 1, self.x + 2])
                elif self.y + 1 < 8 and plansza[self.y + 1, self.x + 2].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 1, self.x + 2])
        return self.ruchy


class Krol(Figura):
    znak = 'k'

    def __init__(self, pozycja, cz_b):
        Figura.__init__(self, pozycja, cz_b)

    def mozliwe_ruchy(self, plansza):
        if self.znak[:-1] == figura_czerwona:
            if self.y-1 >= 0 and plansza[self.y - 1, self.x].znak[:-1] == puste_pole:      # gora
                self.ruchy.append([self.y - 1, self.x])
            elif self.y-1 >= 0 and plansza[self.y - 1, self.x].znak[:-1] == figura_niebieska:
                self.ruchy.append([self.y - 1, self.x])

            if self.y+1 < 8 and plansza[self.y + 1, self.x].znak[:-1] == puste_pole:         # dol
                self.ruchy.append([self.y + 1, self.x])
            elif self.y+1 < 8 and plansza[self.y + 1, self.x].znak[:-1] == figura_niebieska:
                self.ruchy.append([self.y + 1, self.x])

            if self.x-1 >= 0 and plansza[self.y, self.x - 1].znak[:-1] == puste_pole:          # lewo
                self.ruchy.append([self.y, self.x - 1])
            elif self.x-1 >= 0 and plansza[self.y, self.x - 1].znak[:-1] == figura_niebieska:
                self.ruchy.append([self.y, self.x - 1])

            if self.x+1 < 8 and plansza[self.y, self.x + 1].znak[:-1] == puste_pole:          # prawo
                self.ruchy.append([self.y, self.x + 1])
            elif self.x+1 < 8 and plansza[self.y, self.x + 1].znak[:-1] == figura_niebieska:
                self.ruchy.append([self.y, self.x + 1])

            if self.y-1 >= 0:
                if self.x - 1 >= 0 and plansza[self.y - 1, self.x - 1].znak[:-1] == puste_pole:      # gora lewo
                    self.ruchy.append([self.y - 1, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y - 1, self.x - 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y - 1, self.x - 1])

                if self.x + 1 >= 0 and plansza[self.y - 1, self.x + 1].znak[:-1] == puste_pole:      # gora prawo
                    self.ruchy.append([self.y - 1, self.x + 1])
                elif self.x + 1 >= 0 and plansza[self.y - 1, self.x + 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y - 1, self.x + 1])

            if self.y+1 < 8:
                if self.x - 1 >= 0 and plansza[self.y + 1, self.x - 1].znak[:-1] == puste_pole:      # dół lewo
                    self.ruchy.append([self.y + 1, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y + 1, self.x - 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y + 1, self.x - 1])

                if self.x + 1 >= 0 and plansza[self.y + 1, self.x + 1].znak[:-1] == puste_pole:      # dół prawo
                    self.ruchy.append([self.y + 1, self.x + 1])
                elif self.x + 1 >= 0 and plansza[self.y + 1, self.x + 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y + 1, self.x + 1])

        if self.znak[:-1] == figura_niebieska:
            if self.y-1 >= 0 and plansza[self.y - 1, self.x].znak[:-1] == puste_pole:      # gora
                self.ruchy.append([self.y - 1, self.x])
            elif self.y-1 >= 0 and plansza[self.y - 1, self.x].znak[:-1] == figura_czerwona:
                self.ruchy.append([self.y - 1, self.x])

            if self.y+1 < 8 and plansza[self.y + 1, self.x].znak[:-1] == puste_pole:         # dol
                self.ruchy.append([self.y + 1, self.x])
            elif self.y+1 < 8 and plansza[self.y + 1, self.x].znak[:-1] == figura_czerwona:
                self.ruchy.append([self.y + 1, self.x])

            if self.x-1 >= 0 and plansza[self.y, self.x - 1].znak[:-1] == puste_pole:          # lewo
                self.ruchy.append([self.y, self.x - 1])
            elif self.x-1 >= 0 and plansza[self.y, self.x - 1].znak[:-1] == figura_czerwona:
                self.ruchy.append([self.y, self.x - 1])

            if self.x+1 < 8 and plansza[self.y, self.x + 1].znak[:-1] == puste_pole:          # prawo
                self.ruchy.append([self.y, self.x + 1])
            elif self.x+1 < 8 and plansza[self.y, self.x + 1].znak[:-1] == figura_czerwona:
                self.ruchy.append([self.y, self.x + 1])

            if self.y-1 >= 0:
                if self.x - 1 >= 0 and plansza[self.y - 1, self.x - 1].znak[:-1] == puste_pole:      # gora lewo
                    self.ruchy.append([self.y - 1, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y - 1, self.x - 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y - 1, self.x - 1])

                if self.x + 1 >= 0 and plansza[self.y - 1, self.x + 1].znak[:-1] == puste_pole:      # gora prawo
                    self.ruchy.append([self.y - 1, self.x + 1])
                elif self.x + 1 >= 0 and plansza[self.y - 1, self.x + 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y - 1, self.x + 1])

            if self.y+1 < 8:
                if self.x - 1 >= 0 and plansza[self.y + 1, self.x - 1].znak[:-1] == puste_pole:      # dół lewo
                    self.ruchy.append([self.y + 1, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y + 1, self.x - 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + 1, self.x - 1])

                if self.x + 1 >= 0 and plansza[self.y + 1, self.x + 1].znak[:-1] == puste_pole:      # dół prawo
                    self.ruchy.append([self.y + 1, self.x + 1])
                elif self.x + 1 >= 0 and plansza[self.y + 1, self.x + 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + 1, self.x + 1])
        return self.ruchy


class Hetman(Goniec, Wieza):
    znak = 'h'

    def __init__(self, pozycja, cz_b):
        Figura.__init__(self, pozycja, cz_b)

    def mozliwe_ruchy(self, plansza):
        Goniec.mozliwe_ruchy(self, plansza)
        Wieza.mozliwe_ruchy(self, plansza)

        return self.ruchy


class Pole:
    znak = " "

    def mozliwe_ruchy(self, plansza):
        pass


class Plansza:
    def __init__(self):
        self.plansza = np.empty((9, 9), dtype=object)
        self.plansza[:] = Pole()
        self.plansza[8, :] = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '.'
        for i in range(8):
            self.plansza[i, 8] = str(i + 1)

    def rysuj(self):
        for y in range(8):
            for x in range(8):
                if (x+y) % 2 == 1:
                    print(Back.LIGHTWHITE_EX + '\033[1m' + self.plansza[y, x].znak + ' \033[30m', end="")
                else:
                    print(Back.LIGHTBLACK_EX + '\033[1m' + self.plansza[y, x].znak + ' \033[30m', end="")

                self.plansza[y, x].ruchy = []
            print(self.plansza[y, 8])
        for i in self.plansza[8, :]:
            print(i, end=' ')
        print()

    def pionki(self):
        # niebieskie
        for i in range(8):
            self.plansza[1, i] = Pionek([1, i], True, True)
        self.plansza[0, 0] = Wieza([0, 0], True)
        self.plansza[0, 7] = Wieza([0, 7], True)
        self.plansza[0, 1] = Skoczek([0, 1], True)
        self.plansza[0, 6] = Skoczek([0, 6], True)
        self.plansza[0, 2] = Goniec([0, 2], True)
        self.plansza[0, 5] = Goniec([0, 5], True)
        self.plansza[0, 3] = Hetman([0, 3], True)
        self.plansza[0, 4] = Krol([0, 4], True)

        # czerwone
        for i in range(8):
            self.plansza[6, i] = Pionek([6, i], False, True)
        self.plansza[7, 0] = Wieza([7, 0], False)
        self.plansza[7, 7] = Wieza([7, 7], False)
        self.plansza[7, 1] = Skoczek([7, 1], False)
        self.plansza[7, 6] = Skoczek([7, 6], False)
        self.plansza[7, 2] = Goniec([7, 2], False)
        self.plansza[7, 5] = Goniec([7, 5], False)
        self.plansza[7, 3] = Hetman([7, 3], False)
        self.plansza[7, 4] = Krol([7, 4], False)

    def mozliwe_ruchy_wszystkich(self):
        for y in range(8):
            for x in range(8):
                self.plansza[y, x].mozliwe_ruchy(self.plansza)

    def ruch(self, x, y, figura, x_docelowe, y_docelowe):
        mozliwe_ruchy = self.plansza[y, x].ruchy
        flaga = [i for i in mozliwe_ruchy if i == [y_docelowe, x_docelowe]]

        if self.plansza[y, x].znak == Fore.RED + figura and flaga:      #ruch czerwonych
            if self.plansza[y, x].znak[-1] == 'p':
                self.plansza[y, x].pierwszy_ruch = False

            if self.plansza[y_docelowe, x_docelowe].znak[:-1] == figura_niebieska:
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole()
            else:
                bufor = self.plansza[y_docelowe, x_docelowe]
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = bufor

            self.plansza[y_docelowe, x_docelowe].x = x_docelowe
            self.plansza[y_docelowe, x_docelowe].y = y_docelowe

        if self.plansza[y, x].znak == Fore.BLUE + figura and flaga:      #ruch niebieskich
            if self.plansza[y, x].znak[-1] == 'p':
                self.plansza[y, x].pierwszy_ruch = False

            if self.plansza[y_docelowe, x_docelowe].znak[:-1] == figura_czerwona:
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole()
            else:
                bufor = self.plansza[y_docelowe, x_docelowe]
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = bufor

            self.plansza[y_docelowe, x_docelowe].x = x_docelowe
            self.plansza[y_docelowe, x_docelowe].y = y_docelowe


szachy = Plansza()
szachy.pionki()

while wygrana:
    szachy.rysuj()
    szachy.mozliwe_ruchy_wszystkich()
    try:
        polecenie = input("Podaj ruch: ")
        szachy.ruch(notacja[polecenie[0]], int(polecenie[1]) - 1, polecenie[2], notacja[polecenie[3]],
                    int(polecenie[4]) - 1)
    except:
        # print("ruch nie możliwy do wykonania")
        pass
