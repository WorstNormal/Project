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
from base64 import b64encode as enc64
from base64 import b64decode as dec64
import io
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
		self.setWindowTitle("Самотренажер")
	def main_creat(self):
		x_pos, y_pos = 0, 0
		w_pix, h_pix = 1920, 100
		self.container = QWidget(self)
		self.container.setContentsMargins(0, 0, 0, 0)
		self.container.setFixedSize(w_pix, h_pix)
		self.container.move(x_pos, y_pos)
		self.container.setStyleSheet("background-color:#4483e4;")
		# Текст
		self.label = QLabel("Тренажер для самоподготовки", self)
		self.label.move(710, 25)
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
		self.label_make = QLabel(self)
		self.pixmap_make  = QPixmap()
		self.label_make.setPixmap(self.pixmap_make)
		self.label_make.adjustSize()
		# Текст
		self.str_ans = QLabel(self)
		self.str_ans.setGeometry(360, 450, 1200, 100)
		self.str_ans.setAlignment(QtCore.Qt.AlignCenter)
		self.str_ans.setFont(QFont('Arial', 24))
		self.str_ans.setStyleSheet("QLabel {color: #000000}")
		self.str_ans.hide()
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
		
		self.btn_answer1_make = QPushButton(self)
		self.btn_answer1_make.setGeometry(360, 550, 500, 80)
		self.btn_answer1_make.setStyleSheet(pushButton_StyleSheet)
		self.btn_answer1_make.setObjectName("pushButton")
		self.btn_answer1_make.clicked.connect(self.mmake_answer1)
		self.btn_answer1_make.hide()
		
		self.btn_answer2_make = QPushButton(self)
		self.btn_answer2_make.setGeometry(1060, 550, 500, 80)
		self.btn_answer2_make.setStyleSheet(pushButton_StyleSheet)
		self.btn_answer2_make.setObjectName("pushButton")
		self.btn_answer2_make.clicked.connect(self.mmake_answer2)
		self.btn_answer2_make.hide()
		
		self.btn_answer3_make = QPushButton(self)
		self.btn_answer3_make.setGeometry(360, 650, 500, 80)
		self.btn_answer3_make.setStyleSheet(pushButton_StyleSheet)
		self.btn_answer3_make.setObjectName("pushButton")
		self.btn_answer3_make.clicked.connect(self.mmake_answer3)
		self.btn_answer3_make.hide()
		
		self.btn_answer4_make = QPushButton(self)
		self.btn_answer4_make.setGeometry(1060, 650, 500, 80)
		self.btn_answer4_make.setStyleSheet(pushButton_StyleSheet)
		self.btn_answer4_make.setObjectName("pushButton")
		self.btn_answer4_make.clicked.connect(self.mmake_answer4)
		self.btn_answer4_make.hide()
		
		self.btn_test1_make = QPushButton(self)
		self.btn_test1_make.setGeometry(360, 250, 500, 100)
		self.btn_test1_make.setStyleSheet(pushButton_StyleSheet)
		self.btn_test1_make.clicked.connect(self.make_test1)
		self.btn_test1_make.setObjectName("pushButton")
		self.btn_test1_make.hide()
		
		self.btn_back_make = QPushButton(self)
		self.btn_back_make.setGeometry(860, 800, 200, 100)
		self.btn_back_make.setStyleSheet(pushButton_StyleSheet)
		self.btn_back_make.clicked.connect(self.make_back)
		self.btn_back_make.setObjectName("pushButton")
		self.btn_back_make.setText("Назад")
		self.btn_back_make.hide()
		
		self.btn_next_make = QPushButton(self)
		self.btn_next_make.setGeometry(860, 800, 200, 100)
		self.btn_next_make.setStyleSheet(pushButton_StyleSheet)
		self.btn_next_make.clicked.connect(self.make_next)
		self.btn_next_make.setObjectName("pushButton")
		self.btn_next_make.setText("Продолжить")
		self.btn_next_make.hide()
		
		self.btn_test2_make = QPushButton(self)
		self.btn_test2_make.setGeometry(1060, 250, 500, 100)
		self.btn_test2_make.setStyleSheet(pushButton_StyleSheet)
		self.btn_test2_make.clicked.connect(self.make_test2)
		self.btn_test2_make.setObjectName("pushButton")
		self.btn_test2_make.hide()
		
		self.btn_test3_make = QPushButton(self)
		self.btn_test3_make.setGeometry(360, 600, 500, 100)
		self.btn_test3_make.setStyleSheet(pushButton_StyleSheet)
		self.btn_test3_make.clicked.connect(self.make_test3)
		self.btn_test3_make.setObjectName("pushButton")
		self.btn_test3_make.hide()
		
		self.btn_test4_make = QPushButton(self)
		self.btn_test4_make.setGeometry(1060, 600, 500, 100)
		self.btn_test4_make.setStyleSheet(pushButton_StyleSheet)
		self.btn_test4_make.clicked.connect(self.make_test4)
		self.btn_test4_make.setObjectName("pushButton")
		self.btn_test4_make.hide()
		# Переменные
		self.number_list_make = 0
		self.int_id = 0
	def create_create(self):
		self.x = -125
		self.str_name = QLabel("Введите название:", self)
		self.str_name.setGeometry(790 + self.x, 465, 1000, 100)
		self.str_name.setFont(QFont('Arial', 24))
		self.str_name.setStyleSheet("QLabel {color: #000000}")
		self.str_name.hide()
		
		self.str_coun = QLabel("Введите количество вопросов:", self)
		self.str_coun.setGeometry(790 + self.x, 515, 1000, 100)
		self.str_coun.setFont(QFont('Arial', 24))
		self.str_coun.setStyleSheet("QLabel {color: #000000}")
		self.str_coun.hide()
		# Кнопки
		self.btn_next_create = QPushButton('Продолжить', self)
		self.btn_next_create.setGeometry(860, 750, 200, 100)
		self.btn_next_create.setStyleSheet(pushButton_StyleSheet)
		self.btn_next_create.setObjectName("pushButton")
		self.btn_next_create.clicked.connect(self.create_next)
		self.btn_next_create.hide()
		
		self.btn_back_create = QPushButton('Назад', self)
		self.btn_back_create.setGeometry(860, 900, 200, 100)
		self.btn_back_create.setStyleSheet(pushButton_StyleSheet)
		self.btn_back_create.setObjectName("pushButton")
		self.btn_back_create.clicked.connect(self.create_back)
		self.btn_back_create.hide()
		
		self.btn_take_picter_create = QPushButton('Выбрать Изображение', self)
		self.btn_take_picter_create.setGeometry(430, 750, 300, 100)
		self.btn_take_picter_create.setStyleSheet(pushButton_StyleSheet)
		self.btn_take_picter_create.setObjectName("pushButton")
		self.btn_take_picter_create.clicked.connect(self.create_picter)
		self.btn_take_picter_create.hide()
		# Ввод текста
		self.input_name_create = QTextEdit(self)
		self.input_name_create.setAlignment(QtCore.Qt.AlignCenter)
		self.input_name_create.resize(300, 40)
		self.input_name_create.move(1075 + self.x, 500)
		self.input_name_create.hide()
		self.input_name_create.setStyleSheet(input_StyleSheet)
		
		self.input_coun_create = QTextEdit(self)
		self.input_coun_create.setAlignment(QtCore.Qt.AlignCenter)
		self.input_coun_create.resize(50, 40)
		self.input_coun_create.move(1260 + self.x, 550)
		self.input_coun_create.hide()
		self.input_coun_create.setStyleSheet(input_StyleSheet)
		
		self.input_var1_create = QTextEdit(self)
		self.input_var1_create.setAlignment(QtCore.Qt.AlignCenter)
		self.input_var1_create.resize(300, 40)
		self.input_var1_create.move(1200, 350)
		self.input_var1_create.hide()
		self.input_var1_create.setStyleSheet(input_StyleSheet)
		
		self.input_var2_create = QTextEdit(self)
		self.input_var2_create.setAlignment(QtCore.Qt.AlignCenter)
		self.input_var2_create.resize(300, 40)
		self.input_var2_create.move(1200, 450)
		self.input_var2_create.hide()
		self.input_var2_create.setStyleSheet(input_StyleSheet)
		
		self.input_var3_create = QTextEdit(self)
		self.input_var3_create.setAlignment(QtCore.Qt.AlignCenter)
		self.input_var3_create.resize(300, 40)
		self.input_var3_create.move(1200, 550)
		self.input_var3_create.hide()
		self.input_var3_create.setStyleSheet(input_StyleSheet)
		
		self.input_var4_create = QTextEdit(self)
		self.input_var4_create.setAlignment(QtCore.Qt.AlignCenter)
		self.input_var4_create.resize(300, 40)
		self.input_var4_create.move(1200, 650)
		self.input_var4_create.hide()
		self.input_var4_create.setStyleSheet(input_StyleSheet)
		
		self.input_question_create = QTextEdit(self)
		self.input_question_create.resize(800, 120)
		self.input_question_create.move(300, 570)
		self.input_question_create.hide()
		self.input_question_create.setStyleSheet(input_StyleSheet)
		
		# checkbox
		self.chek_var1_create = QCheckBox(self)
		self.chek_var1_create.resize(40, 40)
		self.chek_var1_create.move(1500, 350)
		self.chek_var1_create.hide()
		self.chek_var1_create.stateChanged.connect(self.create_checkevar1)
		self.chek_var1_create.setStyleSheet(checkbox_StyleSheet)
		
		self.chek_var2_create = QCheckBox(self)
		self.chek_var2_create.resize(40, 40)
		self.chek_var2_create.move(1500, 450)
		self.chek_var2_create.hide()
		self.chek_var2_create.stateChanged.connect(self.create_checkevar2)
		self.chek_var2_create.setStyleSheet(checkbox_StyleSheet)
		
		self.chek_var3_create = QCheckBox(self)
		self.chek_var3_create.resize(40, 40)
		self.chek_var3_create.move(1500, 550)
		self.chek_var3_create.hide()
		self.chek_var3_create.stateChanged.connect(self.create_checkevar3)
		self.chek_var3_create.setStyleSheet(checkbox_StyleSheet)
		
		self.chek_var4_create = QCheckBox(self)
		self.chek_var4_create.resize(40, 40)
		self.chek_var4_create.move(1500, 650)
		self.chek_var4_create.hide()
		self.chek_var4_create.stateChanged.connect(self.create_checkevar4)
		self.chek_var4_create.setStyleSheet(checkbox_StyleSheet)
		# Переменные
		self.fname = ""
		self.int_size_question_create = 0
		self.list_correct_create = [0] * 4
		self.a = self.cur.execute(f"""Select size from test""").fetchall()
		self.int_b = len(self.a)
		self.int_answer1 = 0
		self.int_answer2 = 0
		self.int_answer3 = 0
		self.int_answer4 = 0
		for i in self.a:
			self.int_size_question_create += i[0]
		self.int_ind_create = 0
		# ==========
	# ----------------------------------------------------------------------------------
	def make_test(self):
		self.main_hide()
	def main_window(self):
		self.make_hide()
		self.btn_test1_make.hide(), self.btn_test2_make.hide(), self.btn_test3_make.hide(), self.btn_test4_make.hide()
		self.btn_make_main.show(), self.btn_create_main.show(), self.btn_exit_project.show()
	def main_hide(self):
		self.btn_make_main.hide(), self.btn_create_main.hide(), self.btn_exit_project.hide()
	def exit_project(self):
		self.cur.close()
		exit()
	# ----------------------------------------------------------------------------------
	def make_test_next(self):
		self.number_list_make += 1
		self.make_check_btn()
	def make_back(self):
		self.main_window()
	def make_test_back(self):
		self.number_list_make -= 1
		self.make_check_btn()
	def make_check_btn(self):
		self.max_make = (len(self.list_test) + 3) // 4 - 1
		match self.number_list_make:
			case self.max_make:
				if self.max_make == 0:
					self.btn_left_make.hide()
				self.btn_right_make.hide()
			case 0:
				self.btn_left_make.hide()
			case _:
				self.btn_right_make.show()
				self.btn_left_make.show()
		self.make_name_test()
	
	def make_test(self):
		self.main_hide()
		self.btn_back_make.show(), self.btn_left_make.show(), self.btn_right_make.show()
		self.btn_test1_make.show(), self.btn_test2_make.show(), self.btn_test3_make.show(), self.btn_test4_make.show()
		self.make_name_test()
		self.make_check_btn()
	def make_name_test(self):
		self.btn_test1_make.setText(f"""{self.list_test[self.number_list_make * 4 + 0][1]}
		{self.list_test[self.number_list_make * 4 + 0][2]}""")
		try:
			self.btn_test2_make.show()
			self.btn_test2_make.setText(f"""{self.list_test[self.number_list_make * 4 + 1][1]}
			{self.list_test[self.number_list_make * 4 + 1][2]}""")
		except:
			self.btn_test2_make.hide()
		try:
			self.btn_test3_make.show()
			self.btn_test3_make.setText(f"""{self.list_test[self.number_list_make * 4 + 2][1]}
			{self.list_test[self.number_list_make * 4 + 2][2]}""")
		except:
			self.btn_test3_make.hide()
		try:
			self.btn_test4_make.show()
			self.btn_test4_make.setText(f"""{self.list_test[self.number_list_make * 4 + 3][1]}
			{self.list_test[self.number_list_make * 4 + 3][2]}""")
		except:
			self.btn_test4_make.hide()
	def make_test1(self):
		self.i = 0
		self.make_hide()
		self.base()
		self.mmake_test()
		
	def make_test2(self):
		self.i = 1
		self.make_hide()
		self.base()
		self.mmake_test()
		
	def make_test3(self):
		self.i = 2
		self.make_hide()
		self.base()
		self.mmake_test()
		
	def make_test4(self):
		self.i = 3
		self.make_hide()
		self.base()
		self.mmake_test()
		
	def base(self):
		self.id, self.name, self.coun, self.first = self.list_test[self.number_list_make * 4 + self.i]
		self.id += 2
		self.int_id = 0
		self.list_answer = [""] * self.coun
		self.list_good = self.cur.execute(
			f"""Select cor from question WHERE id >= {self.id} and id < {self.id + self.coun}""").fetchall()
		self.list_var = self.cur.execute(
			f"""Select var1, var2, var3, var4, ques from question WHERE id >= {self.id} and id < {self.id + self.coun}""").fetchall()
		self.btn_answer1_make.show(), self.btn_answer2_make.show()
		self.btn_answer3_make.show(), self.btn_answer4_make.show()
		self.btn_next_make.show(), self.str_ans.show()
		self.mmake_test()
	def mmake_test(self):
		self.btn_answer1_make.setText(str(self.list_var[self.int_id][0]))
		self.btn_answer2_make.setText(str(self.list_var[self.int_id][1]))
		self.btn_answer3_make.setText(str(self.list_var[self.int_id][2]))
		self.btn_answer4_make.setText(str(self.list_var[self.int_id][3]))
		self.str_ans.setText(str(self.list_var[self.int_id][4]))
		
	def mmake_answer1(self):
		if self.int_answer1 == 0:
			self.int_answer1 = 1
			self.btn_answer1_make.setStyleSheet(answer_StyleSheet)
		else:
			self.btn_answer1_make.setStyleSheet(pushButton_StyleSheet)
			self.int_answer1 = 0
		self.mmake_check_answer()
	def mmake_answer2(self):
		if self.int_answer2 == 0:
			self.int_answer2 = 1
			self.btn_answer2_make.setStyleSheet(answer_StyleSheet)
		else:
			self.btn_answer2_make.setStyleSheet(pushButton_StyleSheet)
			self.int_answer2 = 0
		self.mmake_check_answer()
	def mmake_answer3(self):
		if self.int_answer3 == 0:
			self.int_answer3 = 1
			self.btn_answer3_make.setStyleSheet(answer_StyleSheet)
		else:
			self.btn_answer3_make.setStyleSheet(pushButton_StyleSheet)
			self.int_answer3 = 0
		self.mmake_check_answer()
	def mmake_answer4(self):
		if self.int_answer4 == 0:
			self.int_answer4 = 1
			self.btn_answer4_make.setStyleSheet(answer_StyleSheet)
		else:
			self.btn_answer4_make.setStyleSheet(pushButton_StyleSheet)
			self.int_answer4 = 0
		self.mmake_check_answer()
	def mmake_check_answer(self):
		self.list_answer[self.id - self.first + self.int_id] = f"{self.int_answer1} {self.int_answer2} {self.int_answer3} {self.int_answer4}"
	
	def make_hide(self):
		self.btn_test1_make.hide(), self.btn_test2_make.hide(), self.btn_test3_make.hide(), self.btn_test4_make.hide()
		self.btn_back_make.hide(), self.btn_left_make.hide(), self.btn_right_make.hide()
	def make_next(self):
		self.int_id += 1
		self.coun1 = self.coun + 1
		match self.int_id:
			case self.coun1:
				self.main_window()
				self.btn_next_make.hide()
				self.str_ans.hide()
			case self.coun:
				self.btn_answer1_make.hide()
				self.btn_answer2_make.hide()
				self.btn_answer3_make.hide()
				self.btn_answer4_make.hide()
				self.str_ans.hide()
				self.s = 0
				for i in range(self.coun):
					if self.list_answer[i] == self.list_good[i][0]:
						self.s += 1
				self.str_ans.show()
				self.str_ans.setText(f"Процент выполнения = {int(((self.s / self.coun) * 100))}%")
			case _:
				self.btn_answer1_make.setStyleSheet(pushButton_StyleSheet)
				self.btn_answer2_make.setStyleSheet(pushButton_StyleSheet)
				self.btn_answer3_make.setStyleSheet(pushButton_StyleSheet)
				self.btn_answer4_make.setStyleSheet(pushButton_StyleSheet)
				self.int_answer1 = 0
				self.int_answer2 = 0
				self.int_answer3 = 0
				self.int_answer4 = 0
				self.mmake_test()
	#----------------------------------------------------------------------------------
	def create_test(self):
		self.main_hide()
		self.f = True
		self.btn_next_create.show(), #self.btn_back_create.show()
		self.input_name_create.show(), self.input_coun_create.show()
		self.str_name.show(), self.str_coun.show()
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
		self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '',
												 'Картинка (*.png);;Картинка (*.jpg);;Все файлы (*)')[0]
		if (self.fname) != "":
			self.foo = Image.open(self.fname)
			self.foo = self.foo.resize((640 , 360), Image.LANCZOS)
			self.foo.save('data/photo.png')
			with open('data/photo.png', 'rb') as f:
				self.fname = enc64(f.read())
			
	def create_hide(self):
		self.input_var1_create.hide(), self.input_var2_create.hide()
		self.input_var3_create.hide(), self.input_var4_create.hide()
		self.input_question_create.hide(), self.btn_take_picter_create.hide()
		self.chek_var1_create.hide(), self.chek_var2_create.hide()
		self.chek_var3_create.hide(), self.chek_var4_create.hide()
		self.btn_next_create.hide(), self.btn_back_create.hide()
	def create_next(self):
		self.int_ind_create += 1
		self.str_ques = self.input_question_create.toPlainText()
		match self.int_ind_create:
			case 1:
				self.int_coun_create = int(self.input_coun_create.toPlainText()) + 1
				self.list = [0] * int(self.input_coun_create.toPlainText())
				self.cur.execute(f"""INSERT INTO test VALUES ({self.int_b}, '{self.input_name_create.toPlainText()}'
				, {int(self.input_coun_create.toPlainText())}, {self.int_size_question_create + 2})""")
				self.con.commit()
				self.int_b += 1
				self.int_size_question_create += int(self.input_coun_create.toPlainText())
				self.con.commit()
				self.input_name_create.clear(), self.input_coun_create.clear()
				#----
				self.input_name_create.hide(), self.input_coun_create.hide(), self.btn_back_create.hide()
				self.str_coun.hide(), self.str_name.hide()
				self.input_var1_create.show(), self.input_var2_create.show()
				self.input_var3_create.show(), self.input_var4_create.show()
				self.input_question_create.show()
				self.chek_var1_create.show(), self.chek_var2_create.show()
				self.chek_var3_create.show(), self.chek_var4_create.show()
			case self.int_coun_create:
				self.str_var1, self.str_var2, self.str_var3, self.str_var4 = \
					self.input_var1_create.toPlainText(), self.input_var2_create.toPlainText(), \
					self.input_var3_create.toPlainText(), self.input_var4_create.toPlainText()
				self.cur.execute(f"""INSERT INTO question VALUES({self.int_ind_create + self.int_size_question_create},
					"{self.str_ques}", "{self.str_var1}", "{self.str_var2}", "{self.str_var3}",
					"{self.str_var4}", "{" ".join(list(map(str, self.list_correct_create)))}", "{self.fname}")""")
				self.con.commit()
				self.int_ind_create = 0
				self.int_size_question_create += self.int_coun_create
				self.create_hide()
				self.test()
				self.main_window()
			case _:
				#self.btn_back_create.show()
				self.str_var1, self.str_var2, self.str_var3, self.str_var4 = \
					self.input_var1_create.toPlainText(), self.input_var2_create.toPlainText(), \
					self.input_var3_create.toPlainText(), self.input_var4_create.toPlainText()
				if self.list[self.int_ind_create - 2] == 0:
					self.cur.execute(f"""INSERT INTO question VALUES({self.int_ind_create + self.int_size_question_create},
					"{self.str_ques}", "{self.str_var1}", "{self.str_var2}", "{self.str_var3}",
					"{self.str_var4}", "{" ".join(list(map(str, self.list_correct_create)))}", "{self.fname}")""")
					self.con.commit()
					self.list[self.int_ind_create - 2] = 1
				else:
					self.cur.execute(f"""UPDATE question SET var1 = '{self.str_var1}' where id = {self.int_ind_create + self.int_size_question_create}""")
					self.cur.execute(f"""UPDATE question SET var2 = '{self.str_var2}' where id = {self.int_ind_create + self.int_size_question_create}""")
					self.cur.execute(f"""UPDATE question SET var3 = '{self.str_var3}' where id = {self.int_ind_create + self.int_size_question_create}""")
					self.cur.execute(f"""UPDATE question SET var4 = '{self.str_var4}' where id = {self.int_ind_create + self.int_size_question_create}""")
					self.cur.execute(f"""UPDATE question SET question = '{self.str_ques}' where id = {self.int_ind_create + self.int_size_question_create}""")
					self.con.commit()
				self.input_var1_create.clear(), self.input_var2_create.clear()
				self.input_var3_create.clear(), self.input_var4_create.clear()
				self.input_question_create.clear()
				self.chek_var1_create.setChecked(False), self.chek_var2_create.setChecked(False), self.chek_var3_create.setChecked(False), self.chek_var4_create.setChecked(False),
				self.fname = ""
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
			# case _:
			# 	self
	def test(self):
		self.list_test = self.cur.execute(f"""Select * from test""").fetchall()
		
		
if __name__ == '__main__':
	pushButton_StyleSheet = '''
	#pushButton {color: #000000; font: 24px; background-color: #4483e4; border: none; border-radius: 15px;}
	#pushButton:hover {background-color: #78a4e8;}
	#pushButton:pressed {background-color: #686c73;}
	'''
	answer_StyleSheet = '''
	#pushButton {color: #000000; font: 24px; background-color: #686c73; border: none; border-radius: 15px;}
	#pushButton:hover {background-color: #78a4e8;}
	#pushButton:pressed {background-color: #686c73;}
	'''
	input_StyleSheet = "font: 24px"
	checkbox_StyleSheet = """
	QCheckBox:indicator {width:40px; height:40px;}
    QCheckBox:hover {background-color: #78a4e8;}
	QCheckBox:pressed {background-color:  # 686c73;}
	"""
	app = QApplication(sys.argv)
	ex = Window()
	ex.showFullScreen()
	sys.exit(app.exec())
