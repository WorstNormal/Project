from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, \
	QTextEdit, QVBoxLayout, QHBoxLayout, QLineEdit, QCheckBox, QMainWindow
from PyQt5 import QtWidgets, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QFileDialog,
    QGridLayout,
    QPushButton,
    QLabel,
    QListWidget)
import os
import sys
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtWidgets import QInputDialog
import sqlite3
from PIL import Image
class Window(QWidget):
	def __init__(self):
		self.con = sqlite3.connect("database.db")
		self.cur = self.con.cursor()
		super().__init__()
		self.main_creat()
		self.make_create()
		self.create_create()
		self.main_window()
		self.test()
	def main_creat(self):
		x_pos, y_pos = 0, 0
		w_pix, h_pix = 1920, 100
		self.container = QWidget(self)
		self.container.setContentsMargins(0, 0, 0, 0)
		self.container.setFixedSize(w_pix, h_pix)
		self.container.move(x_pos, y_pos)
		self.container.setStyleSheet("background-color:#4483e4;")
		# Текст
		self.label = QLabel("Тренажер по Истории России", self)
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
		
		self.btn_test1_make = QPushButton('→', self)
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
		
		self.btn_take_picter_create = QPushButton('Выбрать Изображение', self)
		self.btn_take_picter_create.setGeometry(560, 650, 200, 100)
		self.btn_take_picter_create.setStyleSheet(pushButton_StyleSheet)
		self.btn_take_picter_create.setObjectName("pushButton")
		self.btn_take_picter_create.clicked.connect(self.create_picter)
		self.btn_take_picter_create.hide()
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
		# checkbox
		self.chek_var1_create = QCheckBox(self)
		self.chek_var1_create.resize(50, 50)
		self.chek_var1_create.move(1400, 250)
		self.chek_var1_create.hide()
		self.chek_var1_create.stateChanged.connect(self.create_checkevar1)
		self.chek_var1_create.setStyleSheet(checkbox_StyleSheet)
		
		self.chek_var2_create = QCheckBox(self)
		self.chek_var2_create.resize(50, 50)
		self.chek_var2_create.move(1400, 350)
		self.chek_var2_create.hide()
		self.chek_var2_create.stateChanged.connect(self.create_checkevar2)
		self.chek_var2_create.setStyleSheet(checkbox_StyleSheet)
		
		self.chek_var3_create = QCheckBox(self)
		self.chek_var3_create.resize(50, 50)
		self.chek_var3_create.move(1400, 450)
		self.chek_var3_create.hide()
		self.chek_var3_create.stateChanged.connect(self.create_checkevar3)
		self.chek_var3_create.setStyleSheet(checkbox_StyleSheet)
		
		self.chek_var4_create = QCheckBox(self)
		self.chek_var4_create.resize(50, 50)
		self.chek_var4_create.move(1400, 550)
		self.chek_var4_create.hide()
		self.chek_var4_create.stateChanged.connect(self.create_checkevar4)
		self.chek_var4_create.setStyleSheet(checkbox_StyleSheet)
		# Переменные
		self.fname = ""
		self.int_size_question_create = 0
		self.list_correct_create = [0] * 4
		self.a = self.cur.execute(f"""Select size from test""").fetchall()
		self.b = len(self.a)
		for i in self.a:
			self.int_size_question_create += i[0]
		self.int_ind_create = 0
		# ==========
	# ----------------------------------------------------------------------------------
	def make_test(self):
		self.main_hide()
	def main_window(self):
		self.make_hide()
		self.btn_make_main.show(), self.btn_create_main.show(), self.btn_exit_project.show()
	def main_hide(self):
		self.btn_make_main.hide(), self.btn_create_main.hide(), self.btn_exit_project.hide()
	def exit_project(self):
		self.cur.close()
		exit()
	# ----------------------------------------------------------------------------------
	def make_test_next(self):
		self.number_list_make += 1
		self.check_make_btn()
	def make_test_back(self):
		self.number_list_make -= 1
		self.check_make_btn()
	def check_make_btn(self):
		self.max_make = (len(self.list_test) + 3) // 4 - 1
		match self.number_list_make:
			case self.max_make:
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
		self.f = True
		self.btn_next_create.show(), self.btn_back_create.show(), self.input_name_create.show(), self.input_coun_create.show()
	def create_checkevar1(self, checked):
		if checked:
			self.list_correct_create[0] = 1
		else:
			self.list_correct_create[0] = 0
	
	def create_checkevar2(self, checked):
		if checked:
			self.list_correct_create[1] = 1
		else:
			self.list_correct_create[1] = 0
	
	def create_checkevar3(self, checked):
		if checked:
			self.list_correct_create[2] = 1
		else:
			self.list_correct_create[2] = 0
	
	def create_checkevar4(self, checked):
		if checked:
			self.list_correct_create[3] = 1
		else:
			self.list_correct_create[3] = 0
	def create_picter(self):
		self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
		self.foo = Image.open(self.fname)
		self.foo = self.foo.resize((640 , 360), Image.LANCZOS)
		print(self.fname)
	def create_hide(self):
		self.input_var1_create.hide(), self.input_var2_create.hide(), self.input_var3_create.hide(), self.input_var4_create.hide(),
		self.chek_var1_create.hide(), self.chek_var2_create.hide(), self.chek_var3_create.hide(), self.chek_var4_create.hide(),
		self.btn_next_create.hide(), self.btn_back_create.hide()
	def create_next(self):
		self.int_ind_create += 1
		match self.int_ind_create:
			case 1:
				self.int_coun_create = int(self.input_coun_create.text()) + 1
				self.list = [0] * int(self.input_coun_create.text())
				if self.f:
					self.cur.execute(f"""INSERT INTO test VALUES ({self.b}, '{self.input_name_create.text()}' , {int(self.input_coun_create.text())}, {self.int_size_question_create + 2})""")
					self.f = False
					self.con.commit()
					self.input_name_create.clear(), self.input_coun_create.clear()
				#----
				self.input_name_create.hide(), self.input_coun_create.hide(), self.btn_back_create.hide()
				self.input_var1_create.show(), self.input_var2_create.show(), self.input_var3_create.show(), self.input_var4_create.show()
				self.chek_var1_create.show(), self.chek_var2_create.show(), self.chek_var3_create.show(), self.chek_var4_create.show(),
				#self.btn_take_picter_create.show()
			case self.int_coun_create:
				self.str_var1, self.str_var2, self.str_var3, self.str_var4 = \
					self.input_var1_create.text(), self.input_var2_create.text(), \
					self.input_var3_create.text(), self.input_var4_create.text()
				self.cur.execute(f"""INSERT INTO question VALUES({self.int_ind_create + self.int_size_question_create}, '{self.str_var1}', '{self.str_var2}', '{self.str_var3}', '{self.str_var4}', '{" ".join(list(map(str, self.list_correct_create)))}', '{self.fname}')""")
				self.con.commit()
				self.int_size_question_create += self.int_coun_create
				self.create_hide()
				self.test()
				self.main_window()
			case _:
				self.btn_back_create.show()
				self.str_var1, self.str_var2, self.str_var3, self.str_var4 = \
					self.input_var1_create.text(), self.input_var2_create.text(), \
					self.input_var3_create.text(), self.input_var4_create.text()
				if self.list[self.int_ind_create - 2] == 0:
					self.cur.execute(f"""INSERT INTO question VALUES({self.int_ind_create + self.int_size_question_create}, '{self.str_var1}', '{self.str_var2}', '{self.str_var3}', '{self.str_var4}', '{" ".join(list(map(str, self.list_correct_create)))}', '{self.fname}')""")
					self.con.commit()
					self.list[self.int_ind_create - 2] = 1
				else:
					self.cur.execute(f"""UPDATE question SET var1 = '{self.str_var1}' where id = {self.int_ind_create + self.int_size_question_create}""")
					self.cur.execute(f"""UPDATE question SET var2 = '{self.str_var2}' where id = {self.int_ind_create + self.int_size_question_create}""")
					self.cur.execute(f"""UPDATE question SET var3 = '{self.str_var3}' where id = {self.int_ind_create + self.int_size_question_create}""")
					self.cur.execute(f"""UPDATE question SET var4 = '{self.str_var4}' where id = {self.int_ind_create + self.int_size_question_create}""")
					self.con.commit()
				self.input_var1_create.clear(), self.input_var2_create.clear(), self.input_var3_create.clear(), self.input_var4_create.clear(),
				self.chek_var1_create.setChecked(False), self.chek_var2_create.setChecked(False), self.chek_var3_create.setChecked(False), self.chek_var4_create.setChecked(False),
				#self.fname = ""
	def create_back(self):
		self.int_ind_create -= 1
		match self.int_ind_create:
			case -1:
				self.int_ind_create = 0
				self.main_window()
				self.btn_next_create.hide(), self.btn_back_create.hide(), self.input_name_create.hide(), self.input_coun_create.hide()
			case 1:
				self.btn_back_create.hide()
				#self.input_var1_create.setText(*self.cur.execute(f"""Select question"""))
	def test(self):
		self.list_test = self.cur.execute(f"""Select * from test""").fetchall()
		print(self.list_test)
		
		
if __name__ == '__main__':
	pushButton_StyleSheet = '''
	#pushButton {color: #000000; background-color: #4483e4; border: none; border-radius: 15px;}
	#pushButton:hover {background-color: #78a4e8;}
	#pushButton:pressed {background-color: #686c73;}
	'''
	input_StyleSheet = "font: 24px"
	checkbox_StyleSheet = """
	QCheckBox:indicator {width:50px; height:50px;}
    QCheckBox:hover {background-color: #78a4e8;}
	QCheckBox:pressed {background-color:  # 686c73;}
	"""
	app = QApplication(sys.argv)
	ex = Window()
	ex.showFullScreen()

	sys.exit(app.exec())
