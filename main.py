from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTextEdit, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5 import QtWidgets
import sys
import sqlite3

class Window(QWidget):
	def __init__(self):
		self.con = sqlite3.connect("database.db")
		self.cur = self.con.cursor()
		super().__init__()
		self.main_creat()
		self.make_create()
		self.create_create()
		self.main_window()
	def main_creat(self):
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
	def make_create(self):
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
		# Переменные
		self.number_list_make = 0
	def create_create(self):
		# Кнопки
		self.btn_next_create = QPushButton('Продолжить', self)
		self.btn_next_create.setGeometry(860, 650, 200, 100)
		self.btn_next_create.setStyleSheet(pushButton_StyleSheet)
		self.btn_next_create.setObjectName("pushButton")
		self.btn_next_create.clicked.connect(self.create_next)
		self.btn_next_create.hide()
		
		self.btn_back_create = QPushButton('Назад', self)
		self.btn_back_create.setGeometry(860, 800, 200, 100)
		self.btn_back_create.setStyleSheet(pushButton_StyleSheet)
		self.btn_back_create.setObjectName("pushButton")
		self.btn_back_create.clicked.connect(self.create_back)
		self.btn_back_create.hide()
		# Ввод текста
		self.input_name_create = QLineEdit(self)
		self.input_name_create.resize(300, 50)
		self.input_name_create.move(775, 500)
		self.input_name_create.hide()
		self.input_name_create.setStyleSheet(input_StyleSheet)
		
		self.input_coun_create = QLineEdit(self)
		self.input_coun_create.resize(35, 50)
		self.input_coun_create.move(1100, 500)
		self.input_coun_create.hide()
		self.input_coun_create.setStyleSheet(input_StyleSheet)
		
		self.input_var1_create = QLineEdit(self)
		self.input_var1_create.resize(300, 50)
		self.input_var1_create.move(1100, 250)
		self.input_var1_create.hide()
		self.input_var1_create.setStyleSheet(input_StyleSheet)
		
		self.input_var2_create = QLineEdit(self)
		self.input_var2_create.resize(300, 50)
		self.input_var2_create.move(1100, 350)
		self.input_var2_create.hide()
		self.input_var2_create.setStyleSheet(input_StyleSheet)
		
		self.input_var3_create = QLineEdit(self)
		self.input_var3_create.resize(300, 50)
		self.input_var3_create.move(1100, 450)
		self.input_var3_create.hide()
		self.input_var3_create.setStyleSheet(input_StyleSheet)
		
		self.input_var4_create = QLineEdit(self)
		self.input_var4_create.resize(300, 50)
		self.input_var4_create.move(1100, 550)
		self.input_var4_create.hide()
		self.input_var4_create.setStyleSheet(input_StyleSheet)
		# Переменные
		self.int_ind_create = 0
		self.int_coun_create = 0
		# ==========
	# ----------------------------------------------------------------------------------
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
	# ----------------------------------------------------------------------------------
	def make_test_next(self):
		self.number_list_make += 1
		self.check_make_btn()
	def make_test_back(self):
		self.number_list_make -= 1
		self.check_make_btn()
	def check_make_btn(self):
		match self.number_list_make:
			case 10:
				self.btn_right_make.hide()
			case 0:
				self.btn_left_make.hide()
			case _:
				self.btn_right_make.show()
				self.btn_left_make.show()
	
	def make_test(self):
		self.main_hide()
		self.btn_back_make.show(), self.btn_left_make.show(), self.btn_right_make.show()
		self.check_make_btn()
	
	def make_hide(self):
		self.btn_back_make.hide(), self.btn_left_make.hide(), self.btn_right_make.hide()
	#----------------------------------------------------------------------------------
	def create_test(self):
		self.main_hide()
		self.btn_next_create.show(), self.btn_back_create.show(), self.input_name_create.show(), self.input_coun_create.show()
	
	def create_next(self):
		self.int_ind_create += 1
		match self.int_ind_create:
			case 1:
				self.int_coun_create = int(self.input_coun_create.text()) + 1
				self.input_name_create.hide(), self.input_coun_create.hide(), self.btn_back_create.hide()
				self.input_var1_create.show(), self.input_var2_create.show(), self.input_var3_create.show(), self.input_var4_create.show(),
			case self.int_coun_create:
				self.cur.close()
				exit()
			case _:
				self.btn_back_create.show()
				self.str_var1, self.str_var2, self.str_var3, self.str_var4 = \
					self.input_var1_create.text(), self.input_var1_create.text(), \
					self.input_var1_create.text(), self.input_var1_create.text()
				self.cur.execute(f"""INSERT INTO question VALUES({self.int_ind_create}, 2, 3, 4, 5) """)
				self.con.commit()
				self.input_var1_create.clear(), self.input_var2_create.clear(), self.input_var3_create.clear(), self.input_var4_create.clear(),
	def create_back(self):
		self.int_ind_create -= 1
		match self.int_ind_create:
			case -1:
				self.int_ind_create = 0
				self.main_window()
				self.btn_next_create.hide(), self.btn_back_create.hide(), self.input_name_create.hide(), self.input_coun_create.hide()
			case 0:
				self.input_var1_create.hide(), self.input_var2_create.hide(), self.input_var3_create.hide(), self.input_var4_create.hide()
			case 1:
				self.btn_back_create.hide()
			
if __name__ == '__main__':
	pushButton_StyleSheet = '''
	#pushButton {color: #000000; background-color: #4483e4; border: none; border-radius: 15px;}
	#pushButton:hover {background-color: #78a4e8;}
	#pushButton:pressed {background-color: #686c73;}
	'''
	input_StyleSheet = "font: 24px"
	app = QApplication(sys.argv)
	ex = Window()
	ex.showFullScreen()

	sys.exit(app.exec())
