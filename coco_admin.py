#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import *
import datetime
import sys
import csv

class Window(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle("CocoAdmin")
		self.setMinimumWidth(600)
		#self.setMaximumWidth(600)
		self.setMinimumHeight(600)
		#self.setMaximumHeight(600)

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

		but_stats = QPushButton("Estadisticas")
		but_stats.clicked.connect(self.show_stats)
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

		#CALENDAR
		# calendar = QCalendarWidget()
		# calendar.showToday()
		# calendar.setMinimumDate(date(2018,1,1))
		# calendar.setMaximumDate(date(2020,12,31))
		# layout.addWidget(calendar,1,4)


		# LA TABLA DEJA UN RENGLON EN BLANCO POR CADA FILA CREADA
		#TABLE
		self.tabla = QTableWidget()
		self.tabla.setColumnCount(5)
		self.tabla.setRowCount(1)
		self.tabla.setShowGrid(True)
		self.tabla.setHorizontalHeaderLabels(('Marca','Plataforma','Cantidad','Valor','Fecha'))
		self.tabla.setSortingEnabled(True)
		layout.addWidget(self.tabla,2,0,1,9)
		with open('datos.csv', mode='r') as csv_file:
			datareader = csv.reader(csv_file)
			for index, row in enumerate(datareader):
				print('index:',index)
				rr = self.tabla.rowCount() + 1
				self.tabla.setRowCount(rr)
				for index2, el in enumerate(row):
					print('index2:',index2)
					self.tabla.setItem(index,index2,QTableWidgetItem(el))

	@classmethod
	def show_stats(self):
		"""crea y muestra estadisticas"""
		marcas = []
		plataforma = []
		cantidad = []
		gasto = []
		with open('datos.csv', mode='r') as csv_file:
			datareader = csv.reader(csv_file)
			for index, row in enumerate(datareader):
				for index2, el in enumerate(row):
					if index2 == 0: marcas.append(el)
					if index2 == 1: plataforma.append(el)
					if index2 == 2: cantidad.append(el)
					if index2 == 3: gasto.append(el)

		m = {}
		p = {}
	
		#CORREGIR QUE TOMA COMO DIFERENTES NOMBRES EN UP Y LOWCASE
		for el in marcas:
			el_ = el.lower() 
			temp = marcas.count(el_)
			m[el_] = temp

		for el in plataforma:
			el_ = el.lower()
			temp = plataforma.count(el_)
			p[el_] = temp

		print(m)
		print(p)

		# CORREGIR: NAME LAYOUT IS NOT DEFINED

		for key, value in m.items():
			t = 5
			label = QLabel(key)
			self.layout.addWidget(label,t,0)
			label = QLabel(value)
			self.layout.addWidget(value,t,1)
			t += 1
		
		for key, value in p.items():
			t = 5
			label = QLabel(key)
			self.layout.addWidget(label,t,2)
			label = QLabel(value)
			self.layout.addWidget(value,t,3)
			t += 1
		
		cant = 0
		gast = 0

		for elm in cantidad:
			cant += elm
		for elm in gasto:
			gast += elm

		label = QLabel('Total Prendas : ', cant)
		self.layout.addWidget(label,5,4)
		label = QLabel('Gasto Total : ', gast)
		self.layout.addWidget(label,5,5)
	
	
	def actualizar(self):
		"""actualiza contenido de la tabla"""
		with open('datos.csv', mode='r') as csv_file:
			datareader = csv.reader(csv_file)
			for index, row in enumerate(datareader):
				rr = self.tabla.rowCount() + 1
				self.tabla.setRowCount(rr)
				for index2, el in enumerate(row):
					#print(index,index2)
					self.tabla.setItem(index,index2,QTableWidgetItem(el))


	def date_error(self):
		'''ventana de error en la fecha cargada'''
		alert = QMessageBox(QMessageBox.Information, "Error","La fecha ingresada es incorrecta", QMessageBox.Ok)
		alert.exec_()


	def create(self):
		"""crear entrada en tabla"""
		ma = self.marca.text()
		plat = self.plataforma.text()
		cant = self.cantidad.text()
		val = self.valor.text()
		d = int(self.dia.currentText())
		m = self.mes1.currentIndex() + 1
		a = int(self.anio.currentText())

		try:
			dt = datetime.date(a,m,d)
		except Exception:
			self.date_error()
			return

		lista = [ma,plat,cant,val,dt]

		with open('datos.csv', mode='a') as csv_file:
			datawriter = csv.writer(csv_file, delimiter=",")
			datawriter.writerow(item for item in lista)
			
		self.marca.clear()
		self.plataforma.clear()
		self.cantidad.clear()
		self.valor.clear()
		
		self.actualizar()

		
	


app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())