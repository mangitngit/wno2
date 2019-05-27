from PyQt5.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QApplication, QGraphicsItem, QStyleOptionGraphicsItem
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
import numpy as np
from colorama import *
init(wrap=False)
import itertools
import sys



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


class kolory:
    niebieski = "niebieski"
    czerwony = "czerwony"
    puste_pole = " "


class Figura(QGraphicsItem):
    znak = " "
    def __init__(self, pozycja, cz_b):
        super(QGraphicsItem, self).__init__()
        self.y = pozycja[0]
        self.x = pozycja[1]
        self.pixmap = QPixmap("src/blank.png")
        self.kolor = cz_b

        self.na_planszy_x = self.x * 45
        self.na_planszy_y = self.y * 45
        self.rectF = QtCore.QRectF(self.na_planszy_x, self.na_planszy_y, 45, 45)

    def rysuj(self):
        self.na_planszy_x = self.x * 45
        self.na_planszy_y = self.y * 45
        self.rectF = QtCore.QRectF(self.na_planszy_x, self.na_planszy_y, 45, 45)

    def mozliwe_ruchy(self, plansza):
        return [], []

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        painter.drawTiledPixmap(self.na_planszy_x, self.na_planszy_y, 45, 45, self.pixmap)

    def boundingRect(self):
        return self.rectF

    def mousePressEvent(self, QGraphicsSceneMouseEvent):
        firstScene.ruch_gui(self.x, self.y)


class Pole2(QGraphicsItem):
    def __init__(self, pozycja):
        super(QGraphicsItem, self).__init__()
        #self.setAcceptHoverEvents(True)
        self.y = pozycja[0]
        self.x = pozycja[1]
        self.pixmap = QPixmap("src/blank2.png")

        self.na_planszy_x = self.x * 45
        self.na_planszy_y = self.y * 45
        self.rectF = QtCore.QRectF(self.na_planszy_x, self.na_planszy_y, 45, 45)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        painter.drawTiledPixmap(self.na_planszy_x, self.na_planszy_y, 45, 45, self.pixmap)

    def boundingRect(self):
        return self.rectF


class Pionek(Figura):
    znak = 'p'
    def __init__(self, pozycja, cz_b, pierwszy_ruch):
        Figura.__init__(self, pozycja, cz_b)
        if cz_b == kolory.niebieski:
            self.pixmap = QPixmap("src/pion_c.png")
        elif cz_b == kolory.czerwony:
            self.pixmap = QPixmap("src/pion_b.png")
        else: pass
        self.pierwszy_ruch = pierwszy_ruch

    def mozliwe_ruchy(self, plansza):
        self.ruchy = []
        self.bicie = []
        if self.kolor == kolory.czerwony:
            if self.pierwszy_ruch:
                if plansza[self.y - 2, self.x].kolor == kolory.puste_pole:
                    self.ruchy.append([self.y - 2, self.x])
                if plansza[self.y - 1, self.x].kolor == kolory.puste_pole:
                    self.ruchy.append([self.y - 1, self.x])

                if self.x-1 >= 0 and plansza[self.y - 1, self.x - 1].kolor == kolory.niebieski:
                    self.ruchy.append([self.y - 1, self.x - 1])
                    self.bicie.append([self.y - 1, self.x - 1])
                if self.x+1 < 8 and plansza[self.y - 1, self.x + 1].kolor == kolory.niebieski:
                    self.ruchy.append([self.y - 1, self.x + 1])
                    self.bicie.append([self.y - 1, self.x + 1])
            else:
                if self.y-1 >= 0 and plansza[self.y - 1, self.x].kolor == kolory.puste_pole:            # przód
                    self.ruchy.append([self.y - 1, self.x])

                if self.x-1 >= 0 and plansza[self.y - 1, self.x - 1].kolor == kolory.niebieski:   # bicia
                    self.ruchy.append([self.y - 1, self.x - 1])
                    self.bicie.append([self.y - 1, self.x - 1])
                if self.x+1 < 8 and plansza[self.y - 1, self.x + 1].kolor == kolory.niebieski:
                    self.ruchy.append([self.y - 1, self.x + 1])
                    self.bicie.append([self.y - 1, self.x + 1])
            return self.ruchy, self.bicie

        if self.kolor == kolory.niebieski:
            if self.pierwszy_ruch:
                if plansza[self.y + 2, self.x].kolor == kolory.puste_pole:
                    self.ruchy.append([self.y + 2, self.x])
                if plansza[self.y + 1, self.x].kolor == kolory.puste_pole:
                    self.ruchy.append([self.y + 1, self.x])

                if self.x-1 >= 0 and plansza[self.y + 1, self.x - 1].kolor == kolory.czerwony:
                    self.ruchy.append([self.y + 1, self.x - 1])
                    self.bicie.append([self.y + 1, self.x - 1])
                if self.x+1 < 8 and plansza[self.y + 1, self.x + 1].kolor == kolory.czerwony:
                    self.ruchy.append([self.y + 1, self.x + 1])
                    self.bicie.append([self.y + 1, self.x + 1])
            else:
                if self.y+1 < 8 and plansza[self.y + 1, self.x].kolor == kolory.puste_pole:            # przód
                    self.ruchy.append([self.y + 1, self.x])

                if self.x-1 >= 0 and plansza[self.y + 1, self.x - 1].kolor == kolory.czerwony:   # bicia
                    self.ruchy.append([self.y + 1, self.x - 1])
                    self.bicie.append([self.y + 1, self.x - 1])
                if self.x+1 < 8 and plansza[self.y + 1, self.x + 1].kolor == kolory.czerwony:
                    self.ruchy.append([self.y + 1, self.x + 1])
                    self.bicie.append([self.y + 1, self.x + 1])
            return self.ruchy, self.bicie


class Pole(Figura):
    znak = " "
    kolor = " "

    def __init__(self, pozycja, cz_b):
        Figura.__init__(self, pozycja, cz_b)

    def mozliwe_ruchy(self, plansza):
        return [], []


class Plansza(QWidget):
    wygrana = True
    czer_nieb_ruch = True
    #krol_niebieski = Krol([0, 4], True, True)
    #krol_czerwony = Krol([7, 4], False, True)
    plansza = None
    def __init__(self):
        QWidget.__init__(self)
        self.scene = QGraphicsScene(self)
        self.board_pixmap = QPixmap("src/board.png")
        self.scene.addPixmap(self.board_pixmap)
        self.view = QGraphicsView(self.scene, self)
        self.view.resize(400, 400)

        self.mozliwe_ruchy_biezacego_pionka = []
        self.mozliwe_bicie_biezacego_pionka = []
        self.wszystkie_ruchy = []
        self.wszystkie_bicia = []
        self.ruchy_niebieskich = []
        self.ruchy_czerwonych = []

        self.plansza = np.empty((9, 9), dtype=object)
        self.plansza2 = np.empty((9, 9), dtype=object)
        for x, y in itertools.product(range(9), range(9)):
            self.plansza[y, x] = Pole([y, x], kolory.puste_pole)
        for x, y in itertools.product(range(9), range(9)):
            self.plansza2[y, x] = Pole2([y, x])
        self.plansza[8, :] = ' A', ' B', ' C', ' D', ' E', ' F', ' G', ' H', ' .'
        for i in range(8):
            self.plansza[i, 8] = ' ' + str(i + 1)

        self.pionki()
        self.rysuj([10, 10])
        self.mozliwe_ruchy_wszystkich()
        # self.pole(4, 6)
        # self.rysuj([4, 6])
        # self.ruch(4, 6, 4, 4)
        # self.rysuj([10, 10])
        for x, y in itertools.product(range(8), range(8)):
            self.scene.addItem(self.plansza2[y, x])
        for x, y in itertools.product(range(8), range(8)):
            self.scene.addItem(self.plansza[y, x])
        self.show()

        self.ruszenie = True
        self.wybrane_pole = False

    def ruch_gui(self, x, y):
        if self.ruszenie:
            self.pole(x, y)
            self.rysuj([x, y])
            for pole in self.mozliwe_ruchy_biezacego_pionka:
                self.plansza2[pole[0], pole[1]].pixmap = QPixmap("src/ruch.png")
            for pole in self.mozliwe_bicie_biezacego_pionka:
                self.plansza2[pole[0], pole[1]].pixmap = QPixmap("src/bicie.png")

            self.prev_x = x
            self.prev_y = y
            self.ruszenie = False
            self.wybrane_pole = True

            self.scene.update()

        elif self.wybrane_pole:

            for pole in self.mozliwe_ruchy_biezacego_pionka:
                self.plansza2[pole[0], pole[1]].pixmap = QPixmap("src/blank2.png")
            for pole in self.mozliwe_bicie_biezacego_pionka:
                self.plansza2[pole[0], pole[1]].pixmap = QPixmap("src/blank2.png")

            # self.plansza[self.prev_y, self.prev_x].setPos((x-self.prev_x)*45, (y-self.prev_y)*45)
            # self.plansza[y, x].setPos((self.prev_x-x) * 45, (self.prev_y-y) * 45)
            #self.plansza[y, x].pixmap, self.plansza[self.prev_y, self.prev_x].pixmap = self.plansza[self.prev_y, self.prev_x].pixmap, self.plansza[y, x].pixmap
            # self.plansza[y, x].y, self.plansza[self.prev_y, self.prev_x].y = self.plansza[self.prev_y, self.prev_x].y, self.plansza[y, x].y
            # self.plansza[y, x].x, self.plansza[self.prev_y, self.prev_x].x = self.plansza[self.prev_y, self.prev_x].x, self.plansza[y, x].x
            # self.plansza[y, x].rect()
            # self.plansza[self.prev_y, self.prev_x].rect()

            self.ruszenie = True
            self.wybrane_pole = False

            self.ruch(self.prev_x, self.prev_y, x, y)
            self.rysuj([10, 10])
            self.mozliwe_ruchy_wszystkich()

            self.scene.update()

    def rysuj(self, polecenie):
        for y in range(8):
            for x in range(8):
                flaga1 = [i for i in self.mozliwe_bicie_biezacego_pionka if i == [y, x]]
                flaga2 = [i for i in self.mozliwe_ruchy_biezacego_pionka if i == [y, x]]
                symbol = self.plansza[y, x].znak
                if self.plansza[y, x].kolor == kolory.czerwony: symbol = Fore.RED + symbol
                if self.plansza[y, x].kolor == kolory.niebieski: symbol = Fore.BLUE + symbol
                if [x, y] == [int(polecenie[0]), int(polecenie[1])]:
                    print(Back.LIGHTGREEN_EX + '\033[1m' + ' ' + Back.LIGHTGREEN_EX + symbol + ' \033[30m', end="")
                elif flaga1:
                    print(Back.LIGHTBLUE_EX + '\033[1m' + ' ' + Back.LIGHTBLUE_EX + symbol + ' \033[30m', end="")
                elif flaga2:
                    print(Back.LIGHTYELLOW_EX + '\033[1m' + ' ' + Back.LIGHTYELLOW_EX + symbol + ' \033[30m', end="")
                elif (x+y) % 2 == 1:
                    print(Back.LIGHTWHITE_EX + '\033[1m' + ' ' + Back.LIGHTWHITE_EX + symbol + ' \033[30m', end="")
                else:
                    print(Back.LIGHTBLACK_EX + '\033[1m' + ' ' + Back.LIGHTBLACK_EX + symbol + ' \033[30m', end="")

                self.plansza[y, x].ruchy = []
                self.plansza[y, x].bicie = []
            print(self.plansza[y, 8])
        for i in self.plansza[8, :]:
            print(i, end=' ')
        print()

    def pionki(self):           # białe - false
        #self.plansza[2, 4] = Wieza([2, 4], True, True)
        self.plansza[6, 4] = Pionek([6, 4], kolory.czerwony, True)
        self.plansza[6, 3] = Pionek([6, 3], kolory.czerwony, True)
        self.plansza[6, 2] = Pionek([6, 2], kolory.czerwony, True)
        self.plansza[6, 1] = Pionek([6, 1], kolory.czerwony, True)


        self.plansza[5, 5] = Pionek([5, 5], kolory.niebieski, True)
        self.plansza[1, 3] = Pionek([1, 3], kolory.niebieski, True)
        self.plansza[1, 2] = Pionek([1, 2], kolory.niebieski, True)
        self.plansza[1, 1] = Pionek([1, 1], kolory.niebieski, True)


        # niebieskie
        # for i in range(8):
        #     self.plansza[1, i] = Pionek([1, i], True, True)
        # self.plansza[0, 0] = Wieza([0, 0], True, True)
        # self.plansza[0, 7] = Wieza([0, 7], True, True)
        # self.plansza[0, 1] = Skoczek([0, 1], True)
        # self.plansza[0, 6] = Skoczek([0, 6], True)
        # self.plansza[0, 2] = Goniec([0, 2], True)
        # self.plansza[0, 5] = Goniec([0, 5], True)
        # self.plansza[0, 3] = Hetman([0, 3], True)
        # self.plansza[0, 4] = self.krol_niebieski

        # czerwone
        # for i in range(8):
        #     self.plansza[6, i] = Pionek([6, i], False, True)
        # self.plansza[7, 0] = Wieza([7, 0], False, True)
        # self.plansza[7, 7] = Wieza([7, 7], False, True)
        # self.plansza[7, 1] = Skoczek([7, 1], False)
        # self.plansza[7, 6] = Skoczek([7, 6], False)
        # self.plansza[7, 2] = Goniec([7, 2], False)
        # self.plansza[7, 5] = Goniec([7, 5], False)
        # self.plansza[7, 3] = Hetman([7, 3], False)
        # self.plansza[7, 4] = self.krol_czerwony

    def mozliwe_ruchy_wszystkich(self):
        self.wszystkie_bicia = []
        self.wszystkie_ruchy = []
        for y in range(8):
            for x in range(8):
                ruch, bicie = self.plansza[y, x].mozliwe_ruchy(self.plansza)
                self.wszystkie_bicia.append(bicie)
                self.wszystkie_ruchy.append(ruch)
                if self.plansza[y, x].kolor == kolory.niebieski:
                    self.ruchy_niebieskich.append(ruch)
                if self.plansza[y, x].kolor == kolory.czerwony:
                    self.ruchy_czerwonych.append(ruch)

        buf_wszystkich = []
        for x in self.wszystkie_bicia:
            for y in x:
                buf_wszystkich.append(y)
        # self.krol_czerwony.atakowany = [i for i in buf_wszystkich if i == [self.krol_czerwony.y, self.krol_czerwony.x]]
        # self.krol_niebieski.atakowany = [i for i in buf_wszystkich if i == [self.krol_niebieski.y, self.krol_niebieski.x]]

        # self.szach()

    def pole(self, x, y):
        self.mozliwe_ruchy_biezacego_pionka = self.plansza[y, x].ruchy
        self.mozliwe_bicie_biezacego_pionka = self.plansza[y, x].bicie

    def ruch(self, x, y, x_docelowe, y_docelowe):
        flaga = [i for i in self.mozliwe_ruchy_biezacego_pionka if i == [y_docelowe, x_docelowe]]
        self.mozliwe_ruchy_biezacego_pionka = []
        self.mozliwe_bicie_biezacego_pionka = []

        if flaga and self.czer_nieb_ruch:      # ruch czerwonych
            if self.plansza[y, x].znak == 'p' or 'w' or 'k':
                self.plansza[y, x].pierwszy_ruch = False
            # if self.plansza[y, x].znak == 'p' and y == 1:
            #     self.plansza[y, x] = Hetman([y, x], True)
            if self.plansza[y, x].znak == 'k' and x_docelowe - x == 2:    # roszada po prawej
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole([y, x], kolory.puste_pole)
                self.plansza[y, x + 1] = self.plansza[y, x + 3]
                self.plansza[y, x + 3] = Pole([y, x + 3], kolory.puste_pole)
            elif self.plansza[y, x].znak == 'k' and x_docelowe - x == -2:
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole([y, x], kolory.puste_pole)
                self.plansza[y, x - 1] = self.plansza[y, x - 4]
                self.plansza[y, x - 4] = Pole([y, x - 4], kolory.puste_pole)
            elif self.plansza[y_docelowe, x_docelowe].kolor == kolory.niebieski:   # bicie
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole([y, x], kolory.puste_pole)
            else:
                self.plansza[y_docelowe, x_docelowe], self.plansza[y, x] = self.plansza[y, x], self.plansza[y_docelowe, x_docelowe]     #ruch
            
            self.plansza[y_docelowe, x_docelowe].x = x_docelowe
            self.plansza[y_docelowe, x_docelowe].y = y_docelowe

            self.plansza[y, x].x = x
            self.plansza[y, x].y = y


            self.plansza[y, x].rysuj()
            self.plansza[y_docelowe, x_docelowe].rysuj()


            self.czer_nieb_ruch = not self.czer_nieb_ruch

        elif flaga and not self.czer_nieb_ruch:      # ruch niebieskich
            if self.plansza[y, x].znak == 'p' or 'w' or 'k':
                self.plansza[y, x].pierwszy_ruch = False
            # if self.plansza[y, x].znak == 'p' and y == 6:
            #     self.plansza[y, x] = Hetman([y, x], True)

            if self.plansza[y, x].znak == 'k' and x_docelowe - x == 2:    # roszada po prawej
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole([y, x], kolory.puste_pole)
                self.plansza[y, x + 1] = self.plansza[y, x + 3]
                self.plansza[y, x + 3] = Pole([y, x + 3], kolory.puste_pole)
            elif self.plansza[y, x].znak == 'k' and x_docelowe - x == -2:
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole([y, x], kolory.puste_pole)
                self.plansza[y, x - 1] = self.plansza[y, x - 4]
                self.plansza[y, x - 4] = Pole([y, x - 4], kolory.puste_pole)
            elif self.plansza[y_docelowe, x_docelowe].kolor == kolory.czerwony:  # bicie
                self.plansza[y_docelowe, x_docelowe] = self.plansza[y, x]
                self.plansza[y, x] = Pole([y, x], kolory.puste_pole)
            else:
                self.plansza[y_docelowe, x_docelowe], self.plansza[y, x] = self.plansza[y, x], self.plansza[y_docelowe, x_docelowe]  # ruch

            self.plansza[y_docelowe, x_docelowe].x = x_docelowe
            self.plansza[y_docelowe, x_docelowe].y = y_docelowe

            self.plansza[y, x].x = x
            self.plansza[y, x].y = y

            self.plansza[y, x].rysuj()
            self.plansza[y_docelowe, x_docelowe].rysuj()

    # def szach(self):
    #     if self.krol_czerwony.atakowany: #or self.krol_niebieski.atakowany:
    #         print("SZACH", end=' ')
    #
    #         buf_niebieskich = []
    #         for x in self.ruchy_niebieskich:
    #             for y in x:
    #                 buf_niebieskich.append(y)
    #         flaga1 = False
    #         for ruch in self.krol_czerwony.ruchy:
    #             flaga2 = [i for i in buf_niebieskich if i == ruch]
    #             if not flaga2:
    #                 flaga1 = True
    #         if not flaga1:
    #             print("MAT - wygrana niebieskich")
    #             self.wygrana = False
    #         else:
    #             print()
    #     if self.krol_niebieski.atakowany: #or self.krol_niebieski.atakowany:
    #         print("SZACH", end=' ')
    #
    #         buf_czerwonych = []
    #         for x in self.ruchy_czerwonych:
    #             for y in x:
    #                 buf_czerwonych.append(y)
    #         flaga1 = False
    #         for ruch in self.krol_niebieski.ruchy:
    #             flaga2 = [i for i in buf_czerwonych if i == ruch]
    #             if not flaga2:
    #                 flaga1 = True
    #         if not flaga1:
    #             print("MAT - wygrana czerwonych")
    #             self.wygrana = False
    #         else:
    #             print()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    firstScene = Plansza()
    sys.exit(app.exec_())
