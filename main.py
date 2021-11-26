from PyQt5 import uic
import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget


class Form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_ellipse(self, qp):
        a = random.randrange(100, 200)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(100, 50, a, a)
        a = random.randrange(100, 200)
        qp.drawEllipse(400, 50, a, a)
        a = random.randrange(100, 200)
        qp.drawEllipse(100, 400, a, a)
        a = random.randrange(100, 200)
        qp.drawEllipse(400, 400, a, a)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())