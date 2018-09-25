#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import *
from datetime import date
import sys
import csv

class Window(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle("CocoAdmin")
		self.setMinimumWidth(600)
		self.setMaximumWidth(600)
		self.setMinimumHeight(600)
		self.setMaximumHeight(600)

		#QGRID
		layout = QGridLayout()
		self.setLayout(layout)

		#IMAGE
		label = QLabel(self)
		logo = QPixmap('Etiqueta2.jpg')
		smaller_logo = logo.scaled(160, 80)
		label.setPixmap(smaller_logo)
		layout.addWidget(label,0,2,1,4)
		#label.setAlignment(Qt.AlignHCenter)

		#BUTTON
		button = QPushButton("CREAR")
		button.clicked.connect(self.create)
		layout.addWidget(button,1,8)

		but_today = QPushButton('¿HOY?')
		#but_today.clicked.connect(self.set_date_today)
		layout.addWidget(but_today,1,4)

		but_stats = QPushButton("Estadisticas")
		#but_stats.clicked.connect(self.show_stats)
		layout.addWidget(but_stats,4,0)

		#LINEEDIT
		self.marca = QLineEdit()
		self.marca.setPlaceholderText("Marca")
		layout.addWidget(self.marca,1,0)

		self.plataforma = QLineEdit()
		self.plataforma.setPlaceholderText("Plataforma")
		layout.addWidget(self.plataforma,1,1)

		self.cantidad = QLineEdit()
		self.cantidad.setPlaceholderText("Cantidad")
		layout.addWidget(self.cantidad,1,2)

		self.valor = QLineEdit()
		self.valor.setPlaceholderText("Valor")
		layout.addWidget(self.valor,1,3)

		#COMBOBOX
		self.dia = QComboBox()
		for num in range(31):
			self.dia.addItem(str(num+1))
		layout.addWidget(self.dia,1,5)

		self.mes1 = QComboBox()
		meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
		for mes in meses:
			self.mes1.addItem(mes)
		layout.addWidget(self.mes1,1,6)

		self.anio = QComboBox()
		for num in range(2017,2020):
			self.anio.addItem(str(num))
		layout.addWidget(self.anio,1,7)

		#TABLE
		self.tabla = QTableWidget()
		self.tabla.setColumnCount(5)
		self.tabla.setRowCount(0)
		self.tabla.setShowGrid(True)
		self.tabla.setHorizontalHeaderLabels(('Marca','Plataforma','Cantidad','Valor','Fecha'))
		layout.addWidget(self.tabla,2,0,1,9)
		with open('datos.csv', mode='r') as csv_file:
			datareader = csv.reader(csv_file)
			for index, row in enumerate(datareader):
				rr = self.tabla.rowCount() + 1
				self.tabla.setRowCount(rr)
				for index2, el in enumerate(row):
					self.tabla.setItem(index,index2,QTableWidgetItem(el))
		
		
	#FUNCION SET_DATE_TODAY
	def set_date_today(self):
		



	#FUNCION ESTADISTICAS
	# def show_stats(self):
	# 	with open('datos.csv', mode='r') as csv_file:
	# 		datareader = csv.reader(csv_file)
	# 		for index, row in enumerate(datareader):
	# 			for el in row:
	

	#FUNCION LEER
	def actualizar(self):
		with open('datos.csv', mode='r') as csv_file:
			datareader = csv.reader(csv_file)
			for index, row in enumerate(datareader):
				rr = self.tabla.rowCount() + 1
				self.tabla.setRowCount(rr)
				for index2, el in enumerate(row):
					#print(index,index2)
					self.tabla.setItem(index,index2,QTableWidgetItem(el))

	#FUNCION CREAR
	def create(self):
		ma = self.marca.text()
		plat = self.plataforma.text()
		cant = self.cantidad.text()
		val = self.valor.text()
		d = self.dia.currentText()
		m = self.mes1.currentText()
		a = self.anio.currentText()

		lista = [ma,plat,cant,val,[d,m,a]]

		with open('datos.csv', mode='a') as csv_file:
			datawriter = csv.writer(csv_file, delimiter=",")
			datawriter.writerow(item for item in lista)
			
		self.marca.clear()
		self.plataforma.clear()
		self.cantidad.clear()
		self.valor.clear()
		self.dia.clear()
		self.mes1.clear()
		self.anio.clear()

		self.actualizar()

		
	


app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())