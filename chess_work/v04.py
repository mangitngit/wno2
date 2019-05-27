from PyQt5.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QApplication, QGraphicsItem, QStyleOptionGraphicsItem
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap

import sys

class Piece(QGraphicsItem):
    def __init__(self, pixmap, x, y):
        super(QGraphicsItem, self).__init__()
        self.pixmap = pixmap
        self.x = x
        self.y = y
        self.rectF = QtCore.QRectF(self.x, self.y, 40, 20)
    def paint(self, painter, QStyleOptionGraphicsItem, widget = None):
        painter.drawTiledPixmap(self.x, self.y, 45, 45, self.pixmap)

    def boundingRect(self):
        return self.rectF

    def mousePressEvent(self, QGraphicsSceneMouseEvent):
        print(self.x/45, self.y/45)
        print(QGraphicsSceneMouseEvent.screenPos())


class MyFirstScene(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.scene = QGraphicsScene(self)
        self.pixmap = QPixmap("board.png")
        self.scene.addPixmap(self.pixmap)

        wieza = Piece(QPixmap("wieza_b.png"), 0 * 45, 0 * 45)

        self.scene.addItem(wieza)
        self.scene.addItem(Piece(QPixmap("kon_b.png"), 1 * 45, 0 * 45))
        self.scene.addItem(Piece(QPixmap("goniec_b.png"), 2 * 45, 0 * 45))
        self.scene.addItem(Piece(QPixmap("krol_b.png"), 3 * 45, 0 * 45))
        self.scene.addItem(Piece(QPixmap("hetman_b.png"), 4 * 45, 0 * 45))
        self.scene.addItem(Piece(QPixmap("goniec_b.png"), 5 * 45, 0 * 45))
        self.scene.addItem(Piece(QPixmap("kon_b.png"), 6 * 45, 0 * 45))
        self.scene.addItem(Piece(QPixmap("wieza_b.png"), 7 * 45, 0 * 45))

        self.scene.addItem(Piece(QPixmap("pion_b.png"), 0 * 45, 1 * 45))
        self.scene.addItem(Piece(QPixmap("pion_b.png"), 1 * 45, 1 * 45))
        self.scene.addItem(Piece(QPixmap("pion_b.png"), 2 * 45, 1 * 45))
        self.scene.addItem(Piece(QPixmap("pion_b.png"), 3 * 45, 1 * 45))
        self.scene.addItem(Piece(QPixmap("pion_b.png"), 4 * 45, 1 * 45))
        self.scene.addItem(Piece(QPixmap("pion_b.png"), 5 * 45, 1 * 45))
        self.scene.addItem(Piece(QPixmap("pion_b.png"), 6 * 45, 1 * 45))
        self.scene.addItem(Piece(QPixmap("pion_b.png"), 7 * 45, 1 * 45))

        self.scene.addItem(Piece(QPixmap("wieza_c.png"), 0 * 45, 7 * 45))
        self.scene.addItem(Piece(QPixmap("kon_c.png"), 1 * 45, 7 * 45))
        self.scene.addItem(Piece(QPixmap("goniec_c.png"), 2 * 45, 7 * 45))
        self.scene.addItem(Piece(QPixmap("krol_c.png"), 3 * 45, 7 * 45))
        self.scene.addItem(Piece(QPixmap("hetman_c.png"), 4 * 45, 7 * 45))
        self.scene.addItem(Piece(QPixmap("goniec_c.png"), 5 * 45, 7 * 45))
        self.scene.addItem(Piece(QPixmap("kon_c.png"), 6 * 45, 7 * 45))
        self.scene.addItem(Piece(QPixmap("wieza_c.png"), 7 * 45, 7 * 45))

        self.scene.addItem(Piece(QPixmap("pion_c.png"), 0 * 45, 6 * 45))
        self.scene.addItem(Piece(QPixmap("pion_c.png"), 1 * 45, 6 * 45))
        self.scene.addItem(Piece(QPixmap("pion_c.png"), 2 * 45, 6 * 45))
        self.scene.addItem(Piece(QPixmap("pion_c.png"), 3 * 45, 6 * 45))
        self.scene.addItem(Piece(QPixmap("pion_c.png"), 4 * 45, 6 * 45))
        self.scene.addItem(Piece(QPixmap("pion_c.png"), 5 * 45, 6 * 45))
        self.scene.addItem(Piece(QPixmap("pion_c.png"), 6 * 45, 6 * 45))
        self.scene.addItem(Piece(QPixmap("pion_c.png"), 7 * 45, 6 * 45))




        self.view = QGraphicsView(self.scene, self)
        self.view.resize(400, 400)
        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    firstScene = MyFirstScene()
    sys.exit(app.exec_())