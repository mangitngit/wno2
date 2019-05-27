from PyQt5.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QApplication, QGraphicsItem, QStyleOptionGraphicsItem
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
import numpy as np
import sys
from colorama import *
init(wrap=False)

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

czerwony = "czerwony"              # kolory pionków i puste pole
niebieski = "niebieski"
puste_pole = " "


class Piece(QGraphicsItem):
    def __init__(self, pixmap, x, y):
        super(QGraphicsItem, self).__init__()
        self.pixmap = pixmap
        self.x = x * 45
        self.y = y * 45
        self.rectF = QtCore.QRectF(self.x, self.y, 40, 20)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        painter.drawTiledPixmap(self.x, self.y, 45, 45, self.pixmap)

    def boundingRect(self):
        return self.rectF

    def mousePressEvent(self, QGraphicsSceneMouseEvent):
        print(self.x/45, self.y/45)
        print(QGraphicsSceneMouseEvent.screenPos())


class Pole:
    znak = " "
    kolor = " "

    def mozliwe_ruchy(self, plansza):
        return [], []


class Figura(Piece):
    znak = " "
    def __init__(self, pozycja, kolor_pionka, pixmap):
        Piece.__init__(self, pixmap, pozycja[0], pozycja[1])
        self.y = pozycja[0]
        self.x = pozycja[1]
        self.ruchy = []
        self.bicie = []
        self.kolor = " "
        if kolor_pionka:
            self.kolor = niebieski
        else:
            self.kolor = czerwony

    def mozliwe_ruchy(self, plansza):
        pass


class Pionek(Figura):
    znak = 'p'
    pixmap = QPixmap("wieza_b.png")
    def __init__(self, pozycja, kolor_pionka, pierwszy_ruch):
        Figura.__init__(self, pozycja, kolor_pionka, self.pixmap)
        self.pierwszy_ruch = pierwszy_ruch

    def mozliwe_ruchy(self, plansza):
        if self.kolor == czerwony:
            if self.pierwszy_ruch:
                if plansza[self.y - 2, self.x].kolor == puste_pole:
                    self.ruchy.append([self.y - 2, self.x])
                if plansza[self.y - 1, self.x].kolor == puste_pole:
                    self.ruchy.append([self.y - 1, self.x])

                if self.x-1 >= 0 and plansza[self.y - 1, self.x - 1].kolor == niebieski:
                    self.ruchy.append([self.y - 1, self.x - 1])
                    self.bicie.append([self.y - 1, self.x - 1])
                if self.x+1 < 8 and plansza[self.y - 1, self.x + 1].kolor == niebieski:
                    self.ruchy.append([self.y - 1, self.x + 1])
                    self.bicie.append([self.y - 1, self.x + 1])
            else:
                if self.y-1 >= 0 and plansza[self.y - 1, self.x].kolor == puste_pole:            # przód
                    self.ruchy.append([self.y - 1, self.x])

                if self.x-1 >= 0 and plansza[self.y - 1, self.x - 1].kolor == niebieski:   # bicia
                    self.ruchy.append([self.y - 1, self.x - 1])
                    self.bicie.append([self.y - 1, self.x - 1])
                if self.x+1 < 8 and plansza[self.y - 1, self.x + 1].kolor == niebieski:
                    self.ruchy.append([self.y - 1, self.x + 1])
                    self.bicie.append([self.y - 1, self.x + 1])
            return self.ruchy, self.bicie

        if self.kolor == niebieski:
            if self.pierwszy_ruch:
                if plansza[self.y + 2, self.x].kolor == puste_pole:
                    self.ruchy.append([self.y + 2, self.x])
                if plansza[self.y + 1, self.x].kolor == puste_pole:
                    self.ruchy.append([self.y + 1, self.x])

                if self.x-1 >= 0 and plansza[self.y + 1, self.x - 1].kolor == czerwony:
                    self.ruchy.append([self.y + 1, self.x - 1])
                    self.bicie.append([self.y + 1, self.x - 1])
                if self.x+1 < 8 and plansza[self.y + 1, self.x + 1].kolor == czerwony:
                    self.ruchy.append([self.y + 1, self.x + 1])
                    self.bicie.append([self.y + 1, self.x + 1])
            else:
                if self.y+1 < 8 and plansza[self.y + 1, self.x].kolor == puste_pole:            # przód
                    self.ruchy.append([self.y + 1, self.x])

                if self.x-1 >= 0 and plansza[self.y + 1, self.x - 1].kolor == czerwony:   # bicia
                    self.ruchy.append([self.y + 1, self.x - 1])
                    self.bicie.append([self.y + 1, self.x - 1])
                if self.x+1 < 8 and plansza[self.y + 1, self.x + 1].kolor == czerwony:
                    self.ruchy.append([self.y + 1, self.x + 1])
                    self.bicie.append([self.y + 1, self.x + 1])
            return self.ruchy, self.bicie


class Plansza(QWidget):
        # flaga ruchu niebieskich/czerwonych
    def __init__(self):
        QWidget.__init__(self)

        self.wygrana = True  # flaga wygranej
        self.aktualny_ruch_koloru = True
        # self.krol_niebieski = Krol([0, 4], True, True)
        # self.krol_czerwony = Krol([7, 4], False, True)
        self.mozliwe_ruchy_biezacego_pionka = []
        self.mozliwe_bicie_biezacego_pionka = []
        self.wszystkie_ruchy = []
        self.wszystkie_bicia = []
        self.ruchy_niebieskich = []
        self.ruchy_czerwonych = []

        self.plansza = np.empty((9, 9), dtype=object)  # tworzenie pustej planszy z oznaczeniami
        self.plansza[:] = Pole()
        self.plansza[8, :] = ' A', ' B', ' C', ' D', ' E', ' F', ' G', ' H', ' .'
        for i in range(8):
            self.plansza[i, 8] = ' ' + str(i + 1)


    def rysuj(self, polecenie):  # rysowanie planszy
        for y in range(8):
            for x in range(8):
                flaga1 = [i for i in self.mozliwe_bicie_biezacego_pionka if i == [y, x]]
                flaga2 = [i for i in self.mozliwe_ruchy_biezacego_pionka if i == [y, x]]
                symbol = self.plansza[y, x].znak
                if self.plansza[y, x].kolor == czerwony:
                    symbol = Fore.RED + symbol
                else:
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


    def pionki(self):  # implementacja pionków
        pass
        # # niebieskie
        # for i in range(8):
        #     self.plansza[1, i] = Pionek([1, i], True, True, QPixmap("src/pion_b.png"))
        # self.plansza[0, 0] = Wieza([0, 0], True, True, QPixmap("src/wieza_b.png"))
        # self.plansza[0, 7] = Wieza([0, 7], True, True, QPixmap("src/wieza_b.png"))
        # self.plansza[0, 1] = Skoczek([0, 1], True, QPixmap("src/kon_b.png"))
        # self.plansza[0, 6] = Skoczek([0, 6], True, QPixmap("src/kon_b.png"))
        # self.plansza[0, 2] = Goniec([0, 2], True, QPixmap("src/goniec_b.png"))
        # self.plansza[0, 5] = Goniec([0, 5], True, QPixmap("src/goniec_b.png"))
        # self.plansza[0, 3] = Hetman([0, 3], True, QPixmap("src/hetman_b.png"))
        # self.plansza[0, 4] = self.krol_niebieski
        #
        # # czerwone
        # for i in range(8):
        #     self.plansza[6, i] = Pionek([6, i], False, True, QPixmap("src/pion_c.png"))
        # self.plansza[7, 0] = Wieza([7, 0], False, True, QPixmap("src/wieza_c.png"))
        # self.plansza[7, 7] = Wieza([7, 7], False, True, QPixmap("src/wieza_c.png"))
        # self.plansza[7, 1] = Skoczek([7, 1], False, QPixmap("src/kon_c.png"))
        # self.plansza[7, 6] = Skoczek([7, 6], False, QPixmap("src/kon_c.png"))
        # self.plansza[7, 2] = Goniec([7, 2], False, QPixmap("src/goniec_c.png"))
        # self.plansza[7, 5] = Goniec([7, 5], False, QPixmap("src/goniec_c.png"))
        # self.plansza[7, 3] = Hetman([7, 3], False, QPixmap("src/hetman_c.png"))
        # self.plansza[7, 4] = self.krol_czerwony


    def mozliwe_ruchy_wszystkich(self):
        self.wszystkie_bicia = []
        self.wszystkie_ruchy = []
        for y in range(8):
            for x in range(8):
                ruch, bicie = self.plansza[y, x].mozliwe_ruchy(self.plansza)
                self.wszystkie_bicia.append(bicie)
                self.wszystkie_ruchy.append(ruch)
                if self.plansza[y, x].kolor == niebieski:
                    self.ruchy_niebieskich.append(ruch)
                if self.plansza[y, x].kolor == czerwony:
                    self.ruchy_czerwonych.append(ruch)

        buf_wszystkich = []
        for x in self.wszystkie_bicia:
            for y in x:
                buf_wszystkich.append(y)
        self.krol_czerwony.atakowany = [i for i in buf_wszystkich if i == [self.krol_czerwony.y, self.krol_czerwony.x]]
        self.krol_niebieski.atakowany = [i for i in buf_wszystkich if i == [self.krol_niebieski.y, self.krol_niebieski.x]]

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
                print("MAT")
                self.wygrana = False
            else:
                print()


    def pole(self, x, y):
        self.mozliwe_ruchy_biezacego_pionka = self.plansza[y, x].ruchy
        self.mozliwe_bicie_biezacego_pionka = self.plansza[y, x].bicie


    def ruch(self, x, y, x_docelowe, y_docelowe):
        flaga = [i for i in self.mozliwe_ruchy_biezacego_pionka if i == [y_docelowe, x_docelowe]]
        self.mozliwe_ruchy_biezacego_pionka = []
        self.mozliwe_bicie_biezacego_pionka = []

        if flaga and self.aktualny_ruch_koloru:  # ruch czerwonych
            if self.plansza[y, x].znak == 'p' or 'w' or 'k':
                self.plansza[y, x].pierwszy_ruch = False
            # if self.plansza[y, x].znak == 'p' and y == 1:
            #     self.plansza[y, x] = Hetman([y, x], True)

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
            elif self.plansza[y_docelowe, x_docelowe].kolor == niebieski:  # bicie
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole()
            else:
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]  # ruch
                self.plansza[y, x] = Pole()

            self.plansza[y_docelowe, x_docelowe].x = x_docelowe
            self.plansza[y_docelowe, x_docelowe].y = y_docelowe

            self.aktualny_ruch_koloru = not self.aktualny_ruch_koloru

        elif flaga and not self.aktualny_ruch_koloru:  # ruch niebieskich
            if self.plansza[y, x].znak == 'p' or 'w' or 'k':
                self.plansza[y, x].pierwszy_ruch = False
            # if self.plansza[y, x].znak == 'p' and y == 6:
            #     self.plansza[y, x] = Hetman([y, x], True)

            if self.plansza[y, x].znak == 'k' and x_docelowe - x == 2:  # roszada po prawej
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole()
                self.plansza[y, x + 1] = self.plansza[y, x + 3]
                self.plansza[y, x + 3] = Pole()
            elif self.plansza[y_docelowe, x_docelowe].kolor == czerwony:
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole()
            else:
                bufor = self.plansza[y_docelowe, x_docelowe]
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = bufor

            self.plansza[y_docelowe, x_docelowe].x = x_docelowe
            self.plansza[y_docelowe, x_docelowe].y = y_docelowe

            self.aktualny_ruch_koloru = not self.aktualny_ruch_koloru


class MyFirstScene(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.scene = QGraphicsScene(self)
        self.pixmap = QPixmap("board.png")
        self.scene.addPixmap(self.pixmap)

        wieza = Pionek([0, 0], True, True)

        self.scene.addItem(wieza)
        self.scene.addItem(Piece(QPixmap("kon_b.png"), 1, 0 ))
        self.scene.addItem(Piece(QPixmap("goniec_b.png"), 2, 0))

        self.view = QGraphicsView(self.scene, self)
        self.view.resize(400, 400)
        self.show()


if __name__=="__main__":
    app = QApplication(sys.argv)
    firstScene = MyFirstScene()
    sys.exit(app.exec_())


