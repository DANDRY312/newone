import sys
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pqtb.ui', self)
        self.initUI()

    def initUI(self):
        self.h, self.w = 500, 500
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_cir(qp)
            qp.end()
            self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_cir(self, qp):
        qp.setBrush(QColor("yellow"))
        x1, y1, x2, y2 = random.choice(range(0, self.h + 1)), random.choice(range(0, self.w + 1)), \
                         random.choice(range(0, self.h + 1)), random.choice(range(0, self.w + 1))
        qp.drawEllipse(x1, y1, x2, y2)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())