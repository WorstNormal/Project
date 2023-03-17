from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore
import sys

app = QApplication(sys.argv)
win = QMainWindow()

label = QLabel(win)
pixmap = QPixmap('image.png')
label.setPixmap(pixmap)
label.adjustSize()

win.show()
sys.exit(app.exec_())