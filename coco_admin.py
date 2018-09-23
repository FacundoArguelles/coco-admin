#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle("CocoAdmin")
		self.resize(600,600)

		#QGRID
		layout = QGridLayout()
		self.setLayout(layout)

		#ICON

		#LINEEDIT
		self.lineedit = QLineEdit()
		self.lineedit.setPlaceholderText("Marca")
		layout.addWidget(self.lineedit,0,0)

		self.lineedit = QLineEdit()
		self.lineedit.setPlaceholderText("Plataforma")
		layout.addWidget(self.lineedit,0,1)

		self.lineedit = QLineEdit()
		self.lineedit.setPlaceholderText("Cantidad")
		layout.addWidget(self.lineedit,0,2)

		self.lineedit = QLineEdit()
		self.lineedit.setPlaceholderText("Valor")
		layout.addWidget(self.lineedit,0,3)

		#COMBOBOX
		self.combobox = QComboBox()
		for num in range(31):
			self.combobox.addItem(str(num+1))
		layout.addWidget(self.combobox,0,4)

		self.combobox = QComboBox()
		meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
		for mes in meses:
			self.combobox.addItem(mes)
		layout.addWidget(self.combobox,0,5)

		self.combobox = QComboBox()
		for num in range(1980,2020):
			self.combobox.addItem(str(num))
		layout.addWidget(self.combobox,0,6)


			


app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())