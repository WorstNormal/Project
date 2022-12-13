from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTextEdit, QVBoxLayout, QHBoxLayout
from PyQt5 import QtWidgets
import sys


class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.object()
		self.main_window()
	
	def object(self):
		# -Главная
		# Контейнер
		x_pos, y_pos = 0, 0
		w_pix, h_pix = 1920, 100
		self.container = QWidget(self)
		self.container.setContentsMargins(0, 0, 0, 0)
		self.container.setFixedSize(w_pix, h_pix)
		self.container.move(x_pos, y_pos)
		self.container.setStyleSheet("background-color:#4483e4;")
		# Текст
		self.label = QLabel("Тренажер по математике", self)
		self.label.move(750, 25)
		self.label.setFont(QFont('Arial', 28))
		self.label.setStyleSheet("QLabel {color: #000000}")
		self.hbox = QHBoxLayout(self.container)
		self.hbox.setContentsMargins(10, 10, 0, 0)
		# Кнопки
		self.btn_make_main = QPushButton('Пройти тест', self)
		self.btn_make_main.setGeometry(860, 500, 200, 100)
		self.btn_make_main.setStyleSheet(pushButton_StyleSheet)
		self.btn_make_main.setObjectName("pushButton")
		self.btn_make_main.clicked.connect(self.make_test)
		self.btn_make_main.hide()
		
		self.btn_create_main = QPushButton('Создать тест', self)
		self.btn_create_main.setGeometry(860, 650, 200, 100)
		self.btn_create_main.setStyleSheet(pushButton_StyleSheet)
		self.btn_create_main.setObjectName("pushButton")
		self.btn_create_main.clicked.connect(self.create_test)
		self.btn_create_main.hide()
		
		self.btn_exit_project = QPushButton('Выйти', self)
		self.btn_exit_project.setGeometry(860, 800, 200, 100)
		self.btn_exit_project.setStyleSheet(pushButton_StyleSheet)
		self.btn_exit_project.setObjectName("pushButton")
		self.btn_exit_project.clicked.connect(self.exit_project)
		self.btn_exit_project.hide()
		# - Выбрать тест
		# Кнопки
		self.btn_back_make = QPushButton('Назад', self)
		self.btn_back_make.setGeometry(860, 800, 200, 100)
		self.btn_back_make.setStyleSheet(pushButton_StyleSheet)
		self.btn_back_make.setObjectName("pushButton")
		self.btn_back_make.clicked.connect(self.main_window)
		self.btn_back_make.hide()
		
		self.btn_left_make = QPushButton('←', self)
		self.btn_left_make.setGeometry(750, 800, 100, 50)
		self.btn_left_make.setStyleSheet(pushButton_StyleSheet)
		self.btn_left_make.setObjectName("pushButton")
		self.btn_left_make.clicked.connect(self.make_test_back)
		self.btn_left_make.hide()
		
		self.btn_right_make = QPushButton('→', self)
		self.btn_right_make.setGeometry(1070, 800, 100, 50)
		self.btn_right_make.setStyleSheet(pushButton_StyleSheet)
		self.btn_right_make.setObjectName("pushButton")
		self.btn_right_make.clicked.connect(self.make_test_next)
		self.btn_right_make.hide()
		self.number_list_make = 0
	
	# ==========
	def make_test(self):
		self.main_hide()
	
	def main_window(self):
		self.make_hide()
		self.btn_make_main.show(), self.btn_create_main.show(), self.btn_exit_project.show()
	
	def main_hide(self):
		self.btn_make_main.hide(), self.btn_create_main.hide(), self.btn_exit_project.hide()
	
	@staticmethod
	def exit_project():
		exit()
	
	def make_test_next(self):
		self.number_list_make += 1
		self.check_make_btn()
	
	def make_test_back(self):
		self.number_list_make -= 1
		self.check_make_btn()
	
	def check_make_btn(self):
		if self.number_list_make == 10:
			self.btn_right_make.hide()
		else:
			self.btn_right_make.show()
		
		if self.number_list_make == 0:
			self.btn_left_make.hide()
		else:
			self.btn_left_make.show()
	
	def make_test(self):
		self.main_hide()
		self.btn_back_make.show(), self.btn_left_make.show(), self.btn_right_make.show()
		self.check_make_btn()
	
	def make_hide(self):
		self.btn_back_make.hide(), self.btn_left_make.hide(), self.btn_right_make.hide()
	
	def create_test(self):
		None


if __name__ == '__main__':
	pushButton_StyleSheet = '''
	#pushButton {color: #000000; background-color: #4483e4; border: none; border-radius: 15px;}
	#pushButton:hover {background-color: #78a4e8;}
	#pushButton:pressed {background-color: #686c73;}
	'''
	app = QApplication(sys.argv)
	ex = Window()
	ex.showFullScreen()
	sys.exit(app.exec())
