# from PIL import Image
#
# foo = Image.open('160921_002.jpg')  # My image is a 200x374 jpeg that is 102kb large
# foo = foo.resize((640 , 360), Image.LANCZOS)
# foo.save('160921_0023.jpg', optimize=True, quality=95)  # The saved downsized image size is 22.9kb

## Изображение
# self.pixmap = QPixmap('orig.jpg')
# # Если картинки нет, то QPixmap будет пустым,
# # а исключения не будет
# self.image = QLabel(self)
# self.image.move(80, 60)
# self.image.resize(250, 250)
# # Отображаем содержимое QPixmap в объекте QLabel
# self.image.setPixmap(self.pixmap)


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 841, 511))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("160921_002.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.cat = QtWidgets.QPushButton(self.centralwidget)
        self.cat.setGeometry(QtCore.QRect(0, 510, 411, 41))
        self.cat.setObjectName("cat")
        self.dog = QtWidgets.QPushButton(self.centralwidget)
        self.dog.setGeometry(QtCore.QRect(410, 510, 391, 41))
        self.dog.setObjectName("dog")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.dog.clicked.connect(self.show_dog)
        self.cat.clicked.connect(self.show_cat)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cat.setText(_translate("MainWindow", "CAT"))
        self.dog.setText(_translate("MainWindow", "DOG"))

    def show_dog(self):
        self.photo.setPixmap(QtGui.QPixmap("imgs/160921_002.jpg"))

    def show_cat(self):
        self.photo.setPixmap(QtGui.QPixmap("imgs/160921_002.jpg"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())