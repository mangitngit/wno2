import numpy as np
from colorama import *
init(wrap=False)

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QTextEdit, QFontDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi

"""
[ Y X ]
"""
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


class Figura():
    znak = ""

    def __init__(self, pozycja, cz_b):
        self.y = pozycja[0]
        self.x = pozycja[1]
        self.ruchy = []
        self.bicie = []
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
                    self.bicie.append([self.y - 1, self.x - 1])
                if self.x+1 < 8 and plansza[self.y - 1, self.x + 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y - 1, self.x + 1])
                    self.bicie.append([self.y - 1, self.x + 1])
            else:
                if self.y-1 >= 0 and plansza[self.y - 1, self.x].znak[:-1] == puste_pole:            # przód
                    self.ruchy.append([self.y - 1, self.x])

                if self.x-1 >= 0 and plansza[self.y - 1, self.x - 1].znak[:-1] == figura_niebieska:   # bicia
                    self.ruchy.append([self.y - 1, self.x - 1])
                    self.bicie.append([self.y - 1, self.x - 1])
                if self.x+1 < 8 and plansza[self.y - 1, self.x + 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y - 1, self.x + 1])
                    self.bicie.append([self.y - 1, self.x + 1])
            return self.ruchy, self.bicie

        if self.znak[:-1] == figura_niebieska:
            if self.pierwszy_ruch:
                if plansza[self.y + 2, self.x].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 2, self.x])
                if plansza[self.y + 1, self.x].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 1, self.x])

                if self.x-1 >= 0 and plansza[self.y + 1, self.x - 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + 1, self.x - 1])
                    self.bicie.append([self.y + 1, self.x - 1])
                if self.x+1 < 8 and plansza[self.y + 1, self.x + 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + 1, self.x + 1])
                    self.bicie.append([self.y + 1, self.x + 1])
            else:
                if self.y+1 < 8 and plansza[self.y + 1, self.x].znak[:-1] == puste_pole:            # przód
                    self.ruchy.append([self.y + 1, self.x])

                if self.x-1 >= 0 and plansza[self.y + 1, self.x - 1].znak[:-1] == figura_czerwona:   # bicia
                    self.ruchy.append([self.y + 1, self.x - 1])
                    self.bicie.append([self.y + 1, self.x - 1])
                if self.x+1 < 8 and plansza[self.y + 1, self.x + 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + 1, self.x + 1])
                    self.bicie.append([self.y + 1, self.x + 1])
            return self.ruchy, self.bicie


class Wieza(Figura):
    znak = 'w'

    def __init__(self, pozycja, cz_b, pierwszy_ruch):
        Figura.__init__(self, pozycja, cz_b)
        self.pierwszy_ruch = pierwszy_ruch

    def mozliwe_ruchy(self, plansza):
        if self.znak[:-1] == figura_czerwona:
            for i in range(self.x + 1, 8):                          # w prawo
                if plansza[self.y, i].znak[:-1] == figura_czerwona:
                    break
                elif plansza[self.y, i].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y, i])
                    self.bicie.append([self.y, i])
                    break
                elif plansza[self.y, i].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y, i])

            for i in range(self.x - 1, -1, -1):                          # w lewo
                if plansza[self.y, i].znak[:-1] == figura_czerwona:
                    break
                elif plansza[self.y, i].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y, i])
                    self.bicie.append([self.y, i])
                    break
                elif plansza[self.y, i].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y, i])

            for i in range(self.y + 1, 8):                          # w prawo
                if plansza[i, self.x].znak[:-1] == figura_czerwona:
                    break
                elif plansza[i, self.x].znak[:-1] == figura_niebieska:
                    self.ruchy.append([i, self.x])
                    self.bicie.append([i, self.x])
                    break
                elif plansza[i, self.x].znak[:-1] == puste_pole:
                    self.ruchy.append([i, self.x])

            for i in range(self.y - 1, -1, -1):                          # w lewo
                if plansza[i, self.x].znak[:-1] == figura_czerwona:
                    break
                elif plansza[i, self.x].znak[:-1] == figura_niebieska:
                    self.ruchy.append([i, self.x])
                    self.bicie.append([i, self.x])
                    break
                elif plansza[i, self.x].znak[:-1] == puste_pole:
                    self.ruchy.append([i, self.x])
            return self.ruchy, self.bicie

        if self.znak[:-1] == figura_niebieska:
            for i in range(self.x + 1, 8):                          # w prawo
                if plansza[self.y, i].znak[:-1] == figura_niebieska:
                    break
                elif plansza[self.y, i].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y, i])
                    self.bicie.append([self.y, i])
                    break
                elif plansza[self.y, i].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y, i])

            for i in range(self.x - 1, -1, -1):                          # w lewo
                if plansza[self.y, i].znak[:-1] == figura_niebieska:
                    break
                elif plansza[self.y, i].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y, i])
                    self.bicie.append([self.y, i])
                    break
                elif plansza[self.y, i].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y, i])

            for i in range(self.y + 1, 8):                          # w prawo
                if plansza[i, self.x].znak[:-1] == figura_niebieska:
                    break
                elif plansza[i, self.x].znak[:-1] == figura_czerwona:
                    self.ruchy.append([i, self.x])
                    self.bicie.append([i, self.x])
                    break
                elif plansza[i, self.x].znak[:-1] == puste_pole:
                    self.ruchy.append([i, self.x])

            for i in range(self.y - 1, -1, -1):                          # w lewo
                if plansza[i, self.x].znak[:-1] == figura_niebieska:
                    break
                elif plansza[i, self.x].znak[:-1] == figura_czerwona:
                    self.ruchy.append([i, self.x])
                    self.bicie.append([i, self.x])
                    break
                elif plansza[i, self.x].znak[:-1] == puste_pole:
                    self.ruchy.append([i, self.x])
            return self.ruchy, self.bicie


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
                    self.bicie.append([self.y - buf, i])
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
                    self.bicie.append([self.y - buf, i])
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
                    self.bicie.append([self.y + buf, i])
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
                elif plansza[self.y + buf, i].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y + buf, i])
                    self.bicie.append([self.y + buf, i])
                    break
                elif plansza[self.y + buf, i].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + buf, i])
                buf += 1
            return self.ruchy, self.bicie

        if self.znak[:-1] == figura_niebieska:
            buf = 1
            for i in range(self.x + 1, 8):  # po skosie w górę w prawo
                if self.y - buf < 0:
                    break
                if plansza[self.y - buf, i].znak[:-1] == figura_niebieska:
                    break
                elif plansza[self.y - buf, i].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y - buf, i])
                    self.bicie.append([self.y - buf, i])
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
                    self.bicie.append([self.y - buf, i])
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
                    self.bicie.append([self.y + buf, i])
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
                    self.bicie.append([self.y + buf, i])
                    break
                elif plansza[self.y + buf, i].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + buf, i])
                buf += 1
            return self.ruchy, self.bicie


class Skoczek(Figura):
    znak = 's'

    def __init__(self, pozycja, cz_b):
        Figura.__init__(self, pozycja, cz_b)

    def mozliwe_ruchy(self, plansza):
        if self.znak[:-1] == figura_czerwona:
            if self.y - 2 >= 0:                             # na gorze
                if self.x - 1 >= 0 and plansza[self.y - 2, self.x - 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y - 2, self.x - 1])
                    self.bicie.append([self.y - 2, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y - 2, self.x - 1].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - 2, self.x - 1])

                if self.x + 1 < 8 and plansza[self.y - 2, self.x + 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y - 2, self.x + 1])
                    self.bicie.append([self.y - 2, self.x + 1])
                elif self.x + 1 < 8 and plansza[self.y - 2, self.x + 1].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - 2, self.x + 1])

            if self.y + 2 < 8:                             # na dole
                if self.x - 1 >= 0 and plansza[self.y + 2, self.x - 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y + 2, self.x - 1])
                    self.bicie.append([self.y + 2, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y + 2, self.x - 1].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 2, self.x - 1])

                if self.x + 1 < 8 and plansza[self.y + 2, self.x + 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y + 2, self.x + 1])
                    self.bicie.append([self.y + 2, self.x + 1])
                elif self.x + 1 < 8 and plansza[self.y + 2, self.x + 1].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 2, self.x + 1])

            if self.x - 2 >= 0:                             # po lewej
                if self.y - 1 >= 0 and plansza[self.y - 1, self.x - 2].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y - 1, self.x - 2])
                    self.bicie.append([self.y - 1, self.x - 2])
                elif self.y - 1 >= 0 and plansza[self.y - 1, self.x - 2].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - 1, self.x - 2])

                if self.y + 1 < 8 and plansza[self.y + 1, self.x - 2].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y + 1, self.x - 2])
                    self.bicie.append([self.y + 1, self.x - 2])
                elif self.y + 1 < 8 and plansza[self.y + 1, self.x - 2].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 1, self.x - 2])

            if self.x + 2 < 8:                             # po prawej
                if self.y - 1 >= 0 and plansza[self.y - 1, self.x + 2].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y - 1, self.x + 2])
                    self.bicie.append([self.y - 1, self.x + 2])
                elif self.y - 1 >= 0 and plansza[self.y - 1, self.x + 2].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - 1, self.x + 2])

                if self.y + 1 < 8 and plansza[self.y + 1, self.x + 2].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y + 1, self.x + 2])
                    self.bicie.append([self.y + 1, self.x + 2])
                elif self.y + 1 < 8 and plansza[self.y + 1, self.x + 2].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 1, self.x + 2])
            return self.ruchy, self.bicie

        if self.znak[:-1] == figura_niebieska:
            if self.y - 2 >= 0:                             # na gorze
                if self.x - 1 >= 0 and plansza[self.y - 2, self.x - 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y - 2, self.x - 1])
                    self.bicie.append([self.y - 2, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y - 2, self.x - 1].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - 2, self.x - 1])

                if self.x + 1 < 8 and plansza[self.y - 2, self.x + 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y - 2, self.x + 1])
                    self.bicie.append([self.y - 2, self.x + 1])
                elif self.x + 1 < 8 and plansza[self.y - 2, self.x + 1].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - 2, self.x + 1])

            if self.y + 2 < 8:                             # na dole
                if self.x - 1 >= 0 and plansza[self.y + 2, self.x - 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + 2, self.x - 1])
                    self.bicie.append([self.y + 2, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y + 2, self.x - 1].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 2, self.x - 1])

                if self.x + 1 < 8 and plansza[self.y + 2, self.x + 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + 2, self.x + 1])
                    self.bicie.append([self.y + 2, self.x + 1])
                elif self.x + 1 < 8 and plansza[self.y + 2, self.x + 1].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 2, self.x + 1])

            if self.x - 2 >= 0:                             # po lewej
                if self.y - 1 >= 0 and plansza[self.y - 1, self.x - 2].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y - 1, self.x - 2])
                    self.bicie.append([self.y - 1, self.x - 2])
                elif self.y - 1 >= 0 and plansza[self.y - 1, self.x - 2].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - 1, self.x - 2])

                if self.y + 1 < 8 and plansza[self.y + 1, self.x - 2].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + 1, self.x - 2])
                    self.bicie.append([self.y + 1, self.x - 2])
                elif self.y + 1 < 8 and plansza[self.y + 1, self.x - 2].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 1, self.x - 2])

            if self.x + 2 < 8:                             # po prawej
                if self.y - 1 >= 0 and plansza[self.y - 1, self.x + 2].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y - 1, self.x + 2])
                    self.bicie.append([self.y - 1, self.x + 2])
                elif self.y - 1 >= 0 and plansza[self.y - 1, self.x + 2].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y - 1, self.x + 2])

                if self.y + 1 < 8 and plansza[self.y + 1, self.x + 2].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + 1, self.x + 2])
                    self.bicie.append([self.y + 1, self.x + 2])
                elif self.y + 1 < 8 and plansza[self.y + 1, self.x + 2].znak[:-1] == puste_pole:
                    self.ruchy.append([self.y + 1, self.x + 2])
            return self.ruchy, self.bicie


class Krol(Figura):
    znak = 'k'
    atakowany = False

    def __init__(self, pozycja, cz_b, pierwszy_ruch):
        Figura.__init__(self, pozycja, cz_b)
        self.pierwszy_ruch = pierwszy_ruch

    def mozliwe_ruchy(self, plansza):
        if self.znak[:-1] == figura_czerwona:
            if self.y-1 >= 0 and plansza[self.y - 1, self.x].znak[:-1] == puste_pole:      # gora
                self.ruchy.append([self.y - 1, self.x])
            elif self.y-1 >= 0 and plansza[self.y - 1, self.x].znak[:-1] == figura_niebieska:
                self.ruchy.append([self.y - 1, self.x])
                self.bicie.append([self.y - 1, self.x])

            if self.y+1 < 8 and plansza[self.y + 1, self.x].znak[:-1] == puste_pole:         # dol
                self.ruchy.append([self.y + 1, self.x])
            elif self.y+1 < 8 and plansza[self.y + 1, self.x].znak[:-1] == figura_niebieska:
                self.ruchy.append([self.y + 1, self.x])
                self.bicie.append([self.y + 1, self.x])

            if self.x-1 >= 0 and plansza[self.y, self.x - 1].znak[:-1] == puste_pole:          # lewo
                self.ruchy.append([self.y, self.x - 1])
            elif self.x-1 >= 0 and plansza[self.y, self.x - 1].znak[:-1] == figura_niebieska:
                self.ruchy.append([self.y, self.x - 1])
                self.bicie.append([self.y, self.x - 1])

            if self.x+1 < 8 and plansza[self.y, self.x + 1].znak[:-1] == puste_pole:          # prawo
                self.ruchy.append([self.y, self.x + 1])
            elif self.x+1 < 8 and plansza[self.y, self.x + 1].znak[:-1] == figura_niebieska:
                self.ruchy.append([self.y, self.x + 1])
                self.bicie.append([self.y, self.x + 1])

            if self.y-1 >= 0:
                if self.x - 1 >= 0 and plansza[self.y - 1, self.x - 1].znak[:-1] == puste_pole:      # gora lewo
                    self.ruchy.append([self.y - 1, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y - 1, self.x - 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y - 1, self.x - 1])
                    self.bicie.append([self.y - 1, self.x - 1])

                if self.x + 1 >= 0 and plansza[self.y - 1, self.x + 1].znak[:-1] == puste_pole:      # gora prawo
                    self.ruchy.append([self.y - 1, self.x + 1])
                elif self.x + 1 >= 0 and plansza[self.y - 1, self.x + 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y - 1, self.x + 1])
                    self.bicie.append([self.y - 1, self.x + 1])

            if self.y+1 < 8:
                if self.x - 1 >= 0 and plansza[self.y + 1, self.x - 1].znak[:-1] == puste_pole:      # dół lewo
                    self.ruchy.append([self.y + 1, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y + 1, self.x - 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y + 1, self.x - 1])
                    self.bicie.append([self.y + 1, self.x - 1])

                if self.x + 1 >= 0 and plansza[self.y + 1, self.x + 1].znak[:-1] == puste_pole:      # dół prawo
                    self.ruchy.append([self.y + 1, self.x + 1])
                elif self.x + 1 >= 0 and plansza[self.y + 1, self.x + 1].znak[:-1] == figura_niebieska:
                    self.ruchy.append([self.y + 1, self.x + 1])
                    self.bicie.append([self.y + 1, self.x + 1])

            if self.pierwszy_ruch and plansza[self.y, self.x + 3].znak[-1] == 'w':
                if plansza[self.y, self.x + 3].pierwszy_ruch:
                    if plansza[self.y, self.x + 1].znak[-1] == ' ' and plansza[self.y, self.x + 2].znak[-1] == ' ':
                        self.ruchy.append([self.y, self.x + 2])

            if self.pierwszy_ruch and plansza[self.y, self.x - 4].znak[-1] == 'w':
                if plansza[self.y, self.x - 4].pierwszy_ruch:
                    if plansza[self.y, self.x - 1].znak[-1] == ' ' and plansza[self.y, self.x - 2].znak[-1] == ' ' and plansza[self.y, self.x - 3].znak[-1] == ' ':
                        self.ruchy.append([self.y, self.x - 2])

            return self.ruchy, self.bicie

        if self.znak[:-1] == figura_niebieska:
            if self.y-1 >= 0 and plansza[self.y - 1, self.x].znak[:-1] == puste_pole:      # gora
                self.ruchy.append([self.y - 1, self.x])
            elif self.y-1 >= 0 and plansza[self.y - 1, self.x].znak[:-1] == figura_czerwona:
                self.ruchy.append([self.y - 1, self.x])
                self.bicie.append([self.y - 1, self.x])

            if self.y+1 < 8 and plansza[self.y + 1, self.x].znak[:-1] == puste_pole:         # dol
                self.ruchy.append([self.y + 1, self.x])
            elif self.y+1 < 8 and plansza[self.y + 1, self.x].znak[:-1] == figura_czerwona:
                self.ruchy.append([self.y + 1, self.x])
                self.bicie.append([self.y + 1, self.x])

            if self.x-1 >= 0 and plansza[self.y, self.x - 1].znak[:-1] == puste_pole:          # lewo
                self.ruchy.append([self.y, self.x - 1])
            elif self.x-1 >= 0 and plansza[self.y, self.x - 1].znak[:-1] == figura_czerwona:
                self.ruchy.append([self.y, self.x - 1])
                self.bicie.append([self.y, self.x - 1])

            if self.x+1 < 8 and plansza[self.y, self.x + 1].znak[:-1] == puste_pole:          # prawo
                self.ruchy.append([self.y, self.x + 1])
            elif self.x+1 < 8 and plansza[self.y, self.x + 1].znak[:-1] == figura_czerwona:
                self.ruchy.append([self.y, self.x + 1])
                self.bicie.append([self.y, self.x + 1])

            if self.y-1 >= 0:
                if self.x - 1 >= 0 and plansza[self.y - 1, self.x - 1].znak[:-1] == puste_pole:      # gora lewo
                    self.ruchy.append([self.y - 1, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y - 1, self.x - 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y - 1, self.x - 1])
                    self.bicie.append([self.y - 1, self.x - 1])

                if self.x + 1 >= 0 and plansza[self.y - 1, self.x + 1].znak[:-1] == puste_pole:      # gora prawo
                    self.ruchy.append([self.y - 1, self.x + 1])
                elif self.x + 1 >= 0 and plansza[self.y - 1, self.x + 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y - 1, self.x + 1])
                    self.bicie.append([self.y - 1, self.x + 1])

            if self.y+1 < 8:
                if self.x - 1 >= 0 and plansza[self.y + 1, self.x - 1].znak[:-1] == puste_pole:      # dół lewo
                    self.ruchy.append([self.y + 1, self.x - 1])
                elif self.x - 1 >= 0 and plansza[self.y + 1, self.x - 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + 1, self.x - 1])
                    self.bicie.append([self.y + 1, self.x - 1])

                if self.x + 1 >= 0 and plansza[self.y + 1, self.x + 1].znak[:-1] == puste_pole:      # dół prawo
                    self.ruchy.append([self.y + 1, self.x + 1])
                elif self.x + 1 >= 0 and plansza[self.y + 1, self.x + 1].znak[:-1] == figura_czerwona:
                    self.ruchy.append([self.y + 1, self.x + 1])
                    self.bicie.append([self.y + 1, self.x + 1])

            if self.pierwszy_ruch and plansza[self.y, self.x + 3].znak[-1] == 'w':
                if plansza[self.y, self.x + 3].pierwszy_ruch:
                    if plansza[self.y, self.x + 1].znak[-1] == ' ' and plansza[self.y, self.x + 2].znak[-1] == ' ':
                        self.ruchy.append([self.y, self.x + 2])

            if self.pierwszy_ruch and plansza[self.y, self.x - 4].znak[-1] == 'w':
                if plansza[self.y, self.x - 4].pierwszy_ruch:
                    if plansza[self.y, self.x - 1].znak[-1] == ' ' and plansza[self.y, self.x - 2].znak[-1] == ' ' and plansza[self.y, self.x - 3].znak[-1] == ' ':
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

    def mozliwe_ruchy(self, plansza):
        return [], []


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()
        self.gra = Plansza()
        self.polecenie_1 = ""
        self.polecenie_2 = ""

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        btn_newgame = QPushButton('Nowa Gra', self)
        btn_newgame.setToolTip('Rozpoczyna gre')
        btn_newgame.move(500, 70)
        btn_newgame.clicked.connect(self.on_click)

        btn_exit = QPushButton('Exit', self)
        btn_exit.move(500, 100)
        btn_exit.clicked.connect(self.on_clickk)

        btn_red = QPushButton('Czerwone/Niebieskie', self)
        btn_red.move(500, 130)
        btn_red.clicked.connect(self.on_clickk)

        btn_blue = QPushButton('Pole', self)
        btn_blue.move(500, 160)
        btn_blue.clicked.connect(self.on_click2)

        btn_move = QPushButton('Ruch', self)
        btn_move.move(500, 190)
        btn_move.clicked.connect(self.on_click3)

        self.textbox = QLineEdit(self)
        self.textbox.move(200, 400)
        self.textbox.resize(80, 20)

        self.text = QTextEdit(self)
        self.text.move(50, 50)
        self.text.resize(300, 300)


        self.show()

    #@pyqtSlot()
    def on_clickk(self):
        pass

    def on_click(self):
        self.gra.pionki()
        self.gra.rysuj([10, 10])
        self.text.setText(self.gra.plansza_to_string)
        self.gra.plansza_to_string = ""

    def on_click2(self):
        self.polecenie_1 = self.textbox.text()
        self.gra.mozliwe_ruchy_wszystkich()
        self.gra.pole(notacja[self.polecenie_1[0]], int(self.polecenie_1[1]) - 1)
        self.gra.rysuj([notacja[self.polecenie_1[0]], int(self.polecenie_1[1]) - 1])
        self.text.clear()
        self.text.setText(self.gra.plansza_to_string)
        self.gra.plansza_to_string = ""

    def on_click3(self):
        self.polecenie_2 = self.textbox.text()
        self.gra.ruch(notacja[self.polecenie_1[0]], int(self.polecenie_1[1]) - 1, self.polecenie_2[0],
                    notacja[self.polecenie_2[1]], int(self.polecenie_2[2]) - 1)
        self.gra.rysuj([10, 10])
        self.text.clear()
        self.text.setText(self.gra.plansza_to_string)
        self.gra.plansza_to_string = ""


class Plansza():
    wygrana = True
    czer_nieb_ruch = True
    krol_niebieski = Krol([0, 4], True, True)
    krol_czerwony = Krol([7, 4], False, True)

    def __init__(self):
        self.plansza_to_string = ""

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
                self.plansza_to_string += self.plansza[y, x].znak[-1] + " "
                flaga1 = [i for i in self.mozliwe_bicie_biezacego_pionka if i == [y, x]]
                flaga2 = [i for i in self.mozliwe_ruchy_biezacego_pionka if i == [y, x]]
                if [x, y] == [int(polecenie[0]), int(polecenie[1])]:
                    print(Back.LIGHTGREEN_EX + '\033[1m' + ' ' + Back.LIGHTGREEN_EX + self.plansza[y, x].znak + ' \033[30m', end="")
                    #self.plansza_to_string += Back.LIGHTGREEN_EX + '\033[1m' + ' ' + Back.LIGHTGREEN_EX + self.plansza[y, x].znak + ' \033[30m'
                elif flaga1:
                    print(Back.LIGHTBLUE_EX + '\033[1m' + ' ' + Back.LIGHTBLUE_EX + self.plansza[y, x].znak + ' \033[30m', end="")
                    #self.plansza_to_string += Back.LIGHTBLUE_EX + '\033[1m' + ' ' + Back.LIGHTBLUE_EX + self.plansza[y, x].znak + ' \033[30m'
                elif flaga2:
                    print(Back.LIGHTYELLOW_EX + '\033[1m' + ' ' + Back.LIGHTYELLOW_EX + self.plansza[y, x].znak + ' \033[30m', end="")
                    #self.plansza_to_string += Back.LIGHTYELLOW_EX + '\033[1m' + ' ' + Back.LIGHTYELLOW_EX + self.plansza[y, x].znak + ' \033[30m'
                elif (x+y) % 2 == 1:
                    print(Back.LIGHTWHITE_EX + '\033[1m' + ' ' + Back.LIGHTWHITE_EX + self.plansza[y, x].znak + ' \033[30m', end="")
                    #self.plansza_to_string += Back.LIGHTWHITE_EX + '\033[1m' + ' ' + Back.LIGHTWHITE_EX + self.plansza[y, x].znak + ' \033[30m'
                else:
                    print(Back.LIGHTBLACK_EX + '\033[1m' + ' ' + Back.LIGHTBLACK_EX + self.plansza[y, x].znak + ' \033[30m', end="")
                    #self.plansza_to_string += Back.LIGHTBLACK_EX + '\033[1m' + ' ' + Back.LIGHTBLACK_EX + self.plansza[y, x].znak + ' \033[30m'

                self.plansza[y, x].ruchy = []
                self.plansza[y, x].bicie = []
            print(self.plansza[y, 8])
            self.plansza_to_string += self.plansza[y, 8]
            self.plansza_to_string += '\n'
        for i in self.plansza[8, :]:
            print(i, end=' ')
            self.plansza_to_string += i
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
                if self.plansza[y, x].znak[:-1] == figura_niebieska:
                    self.ruchy_niebieskich.append(ruch)
                if self.plansza[y, x].znak[:-1] == figura_czerwona:
                    self.ruchy_czerwonych.append(ruch)

        buf_wszystkich = []
        for x in self.wszystkie_bicia:
            for y in x:
                buf_wszystkich.append(y)
        self.krol_czerwony.atakowany = [i for i in buf_wszystkich if i == [self.krol_czerwony.y, self.krol_czerwony.x]]
        self.krol_niebieski.atakowany = [i for i in buf_wszystkich if i == [self.krol_niebieski.y, self.krol_niebieski.x]]

        if self.krol_czerwony.atakowany: #or self.krol_niebieski.atakowany:
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
                print("MAT")
                self.wygrana = False
            else:
                print()


    def pole(self, x, y):
        self.mozliwe_ruchy_biezacego_pionka = self.plansza[y, x].ruchy
        self.mozliwe_bicie_biezacego_pionka = self.plansza[y, x].bicie

    def ruch(self, x, y, figura, x_docelowe, y_docelowe):
        flaga = [i for i in self.mozliwe_ruchy_biezacego_pionka if i == [y_docelowe, x_docelowe]]
        self.mozliwe_ruchy_biezacego_pionka = []
        self.mozliwe_bicie_biezacego_pionka = []

        if self.plansza[y, x].znak == Fore.RED + figura and flaga and self.czer_nieb_ruch:      # ruch czerwonych
            if self.plansza[y, x].znak[-1] == 'p' or 'w' or 'k':
                self.plansza[y, x].pierwszy_ruch = False
            if self.plansza[y, x].znak[-1] == 'p' and y == 1:
                self.plansza[y, x] = Hetman([y, x], True)

            if self.plansza[y, x].znak[-1] == 'k' and x_docelowe - x == 2:    # roszada po prawej
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole()
                self.plansza[y, x + 1] = self.plansza[y, x + 3]
                self.plansza[y, x + 3] = Pole()
            elif self.plansza[y, x].znak[-1] == 'k' and x_docelowe - x == -2:
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole()
                self.plansza[y, x - 1] = self.plansza[y, x - 4]
                self.plansza[y, x - 4] = Pole()
            elif self.plansza[y_docelowe, x_docelowe].znak[:-1] == figura_niebieska:   # bicie
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole()
            else:
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]       #ruch
                self.plansza[y, x] = Pole()

            self.plansza[y_docelowe, x_docelowe].x = x_docelowe
            self.plansza[y_docelowe, x_docelowe].y = y_docelowe

            self.czer_nieb_ruch = not self.czer_nieb_ruch

        elif self.plansza[y, x].znak == Fore.BLUE + figura and flaga and not self.czer_nieb_ruch:      # ruch niebieskich
            if self.plansza[y, x].znak[-1] == 'p' or 'w' or 'k':
                self.plansza[y, x].pierwszy_ruch = False
            if self.plansza[y, x].znak[-1] == 'p' and y == 6:
                self.plansza[y, x] = Hetman([y, x], True)

            if self.plansza[y, x].znak[-1] == 'k' and x_docelowe - x == 2:    # roszada po prawej
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole()
                self.plansza[y, x + 1] = self.plansza[y, x + 3]
                self.plansza[y, x + 3] = Pole()
            elif self.plansza[y_docelowe, x_docelowe].znak[:-1] == figura_czerwona:
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole()
            else:
                bufor = self.plansza[y_docelowe, x_docelowe]
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = bufor

            self.plansza[y_docelowe, x_docelowe].x = x_docelowe
            self.plansza[y_docelowe, x_docelowe].y = y_docelowe

            self.czer_nieb_ruch = not self.czer_nieb_ruch

    #def szach(self):




class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

def main():
    wygrana = True
    szachy = Plansza()
    szachy.pionki()

    while True:
        print("="*25)
        szachy.rysuj([10, 10])
        szachy.mozliwe_ruchy_wszystkich()
        if not szachy.wygrana:
            break

        if szachy.czer_nieb_ruch:
            print(Fore.RED+"Ruch czerwonych\033[30m")
        else:
            print(Fore.BLUE+"Ruch niebieskich\033[30m")

        try:
            polecenie_1 = input("Podaj pole: ")

            szachy.pole(notacja[polecenie_1[0]], int(polecenie_1[1]) - 1)
            szachy.rysuj([notacja[polecenie_1[0]], int(polecenie_1[1]) - 1])
            try:
                polecenie_2 = input("Podaj ruch pionka: ")

                szachy.ruch(notacja[polecenie_1[0]], int(polecenie_1[1]) - 1, polecenie_2[0],
                         notacja[polecenie_2[1]], int(polecenie_2[2]) - 1)
            except:
                szachy.mozliwe_bicie_biezacego_pionka = []
                szachy.mozliwe_ruchy_biezacego_pionka = []
                print("Nieprawidlowy ruch")
                pass
        except:
            print("Nieprawidlowe pole")
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()

    #main()
    sys.exit(app.exec_())
