#!/usr/bin/env python3
import datetime
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import *
from db_api import *
from Venta_class import Venta



class Window(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle("CocoAdmin")
		self.setMinimumWidth(600)
		#self.setMaximumWidth(600)
		self.setMinimumHeight(600)
		#self.setMaximumHeight(600)
		self.setStyleSheet('background-color:#ffe2bd;')
		self.setWindowIcon(QIcon('icon.png'))

		#QGRID
		layout = QGridLayout()
		self.setLayout(layout)

		#IMAGE
		label = QLabel(self)
		logo = QPixmap('Etiqueta2.jpg')
		smaller_logo = logo.scaled(160, 80)
		label.setPixmap(smaller_logo)
		label.setStyleSheet('margin-bottom: 10px; margin-left: 50px;')
		layout.addWidget(label,0,2,1,4)
		#label.setAlignment(Qt.AlignHCenter)

		#BUTTON
		button = QPushButton("CREAR")
		button.clicked.connect(self.create)
		layout.addWidget(button,1,8,1,2)
		button.setStyleSheet('background: #ffffff; font: bold;')

		button = QPushButton("BORRAR")
		button.clicked.connect(self.delete)
		layout.addWidget(button,4,9)
		button.setStyleSheet('background-color: red; font: bold;')

		but_stats = QPushButton("Estadisticas")
		but_stats.clicked.connect(self.calc_stats)
		layout.addWidget(but_stats,4,0)
		but_stats.setStyleSheet('background-color:#f1e767; margin-top: 10px; border-width: 3px; border-color: solid gray;')

		#LINEEDIT
		self.marca = QLineEdit()
		self.marca.setPlaceholderText("Marca")
		layout.addWidget(self.marca,1,0)
		self.marca.setStyleSheet('background-color:#f1e767; border-radius: 10px; border: 3px solid gray;')

		self.plataforma = QLineEdit()
		self.plataforma.setPlaceholderText("Plataforma")
		layout.addWidget(self.plataforma,1,1)
		self.plataforma.setStyleSheet('background-color:#f1e767; border-radius: 10px; border: 3px solid gray')

		self.cantidad = QLineEdit()
		self.cantidad.setPlaceholderText("Cantidad")
		layout.addWidget(self.cantidad,1,2)
		self.cantidad.setStyleSheet('background-color:#f1e767; border-radius: 10px; border: 3px solid gray')

		self.valor = QLineEdit()
		self.valor.setPlaceholderText("Valor")
		layout.addWidget(self.valor,1,3)
		self.valor.setStyleSheet('background-color:#f1e767; border-radius: 10px; border: 3px solid gray')

		#COMBOBOX
		self.dia = QComboBox()
		for num in range(31):
			self.dia.addItem(str(num+1))
		layout.addWidget(self.dia,1,5)
		self.dia.setStyleSheet('background-color: #ffffff; ')

		self.mes1 = QComboBox()
		meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
		for mes in meses:
			self.mes1.addItem(mes)
		layout.addWidget(self.mes1,1,6)
		self.mes1.setStyleSheet('background-color: #ffffff; ')

		self.anio = QComboBox()
		for num in range(2017,2020):
			self.anio.addItem(str(num))
		layout.addWidget(self.anio,1,7)
		self.anio.setStyleSheet('background-color: #ffffff; ')
		
		
		# QUE LA ULTIMA ENTRADA CREADA APAREZCA PRIMERA EN LA TABLA, NO ULTIMA
		
		#TABLE
		self.tabla = QTableWidget()
		self.tabla.setColumnCount(6)
		self.tabla.setRowCount(1)
		self.tabla.setShowGrid(True)
		self.tabla.setHorizontalHeaderLabels(('Venta','Marca','Plataforma','Cantidad','Valor','Fecha'))
		self.tabla.setStyleSheet('background-color:#d6f9ff; border-radius: 20px; border: 2px solid gray;')
		#self.tabla.horizontalHeader().setStyleSheet('background-color:#d6f9ff; border-radius: 30px; border: 2px solid gray;')
		self.tabla.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
		self.tabla.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
		self.tabla.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
		self.tabla.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
		self.tabla.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
		self.tabla.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
		#self.tabla.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		#self.tabla.horizontalHeaderItem(0).setStyleSheet('border-radius: 30')
		self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)
		self.tabla.setEditTriggers(self.tabla.NoEditTriggers)
		self.tabla.setSortingEnabled(True)
		self.tabla.verticalHeader().hide()
		'''ya se... no ordena bien el contenido de las columnas, porque los numeros que aparecen
		en realidad son strings.. porque los tengo que convertir porque si no no los muestra'''
		layout.addWidget(self.tabla,2,0,1,10)

		check_table()
		row_count = 1
		for index, row in enumerate(get_all_ventas()):
			#row_count = self.tabla.rowCount() + 1
			self.tabla.setRowCount(row_count)
			for index2, attr in enumerate(row):
				qtwi = QTableWidgetItem()
				qtwi.setData(Qt.EditRole, QVariant(attr))
				self.tabla.setItem(index,index2, qtwi)
			row_count += 1

	
	#FALTA ESTILO VISUAL
	def show_stats(self, marcas, plat, cant, gasto):
		"""crea ventana para mostrar estadisticas"""
		d = QDialog()
		l = QGridLayout()
		d.setLayout(l)
		d.setStyleSheet('background-color:#ffe2bd;')
		label = QLabel('Marcas:')
		l.addWidget(label,0,0)
		label = QLabel('Plataforma:')
		l.addWidget(label,0,2)


		t = 1
		for key, value in marcas.items():
			label = QLabel(str(key))
			l.addWidget(label,t,0)
			label = QLabel(str(value))
			l.addWidget(label,t,1)
			t += 1

		t = 1
		for key, value in plat.items():
			label = QLabel(str(key))
			l.addWidget(label,t,2)
			label = QLabel(str(value))
			l.addWidget(label,t,3)
			t += 1

		label = QLabel('Total Prendas : %i' % (cant))
		l.addWidget(label,5,4)
		label = QLabel('Gasto Total : %i' % (gasto))
		l.addWidget(label,5,5)

		d.exec_()

	
	def calc_stats(self):
		"""crea estadisticas"""
		marcas = []
		plataforma = []
		cantidad = []
		gasto = []

		#lee la db
		for index, row in enumerate(get_all_ventas()):
			for index2, attr in enumerate(row):
				if index2 == 1: marcas.append(attr)
				if index2 == 2: plataforma.append(attr)
				if index2 == 3: cantidad.append(attr)
				if index2 == 4: gasto.append(attr)

		m = {}
		p = {}

		'''pasa los nombres a minusculas para poder contarlos bien y que no cuente como diferentes a los mismos nombres
		ingresados en upper y lower...
		cuenta cantidad de cada nombre'''
		marcas_lower = [el.lower() for el in marcas]
		for el in marcas_lower:
			temp = marcas_lower.count(el)
			m[el] = temp

		plataforma_lower = [el.lower() for el in plataforma]
		for el in plataforma_lower:
			temp = plataforma_lower.count(el)
			p[el] = temp

		cant = 0
		gast = 0

		#Suma gastos y cantidad totales
		for elm in cantidad:
			cant += int(elm)
		for elm in gasto:
			gast += int(elm)

		self.show_stats(m,p,cant,gast)

	
	def actualizar(self, signal=True):
		"""actualiza contenido de la tabla"""
		if signal:
			row_count = self.tabla.rowCount() + 1
			self.tabla.setRowCount(row_count)
		else:
			row_count = self.tabla.rowCount() - 1
			self.tabla.setRowCount(row_count)

		for index, row in enumerate(get_all_ventas()):
			for index2, attr in enumerate(row):
				qtwi = QTableWidgetItem()
				qtwi.setData(Qt.EditRole, QVariant(attr))
				self.tabla.setItem(index,index2, qtwi)


	def date_error(self):
		'''ventana de error en la fecha cargada'''
		alert = QMessageBox(QMessageBox.Information, "Error","La fecha ingresada es incorrecta", QMessageBox.Ok)
		alert.setStyleSheet('background-color:#ffe2bd;')
		alert.exec_()


	def empty_error(self, param):
		'''ventana de error por faltar valores'''
		alert = QMessageBox(QMessageBox.Information, "Error",f" {param} No ha sido completados", QMessageBox.Ok)
		alert.setStyleSheet('background-color:#ffe2bd;')
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

		#Chequeando si estan completas todas las entradas
		check = {'marca': ma, 'plataforma': plat, 'cantidad': cant, 'valor': val}
		param = []
		count = 0

		#contando si faltaron completar campos
		for key, value in check.items():
			if value == '':
				param.append(key)
				count += 1

		if count > 0:
			self.empty_error(param)
			return

		cleaned = {}
		#chequeando si tienen espacios en blanco al principio
		for key, value in check.items():
			cleaned[key] = value.strip()

		#creando la venta para guardar
		try:
			vent = Venta(cleaned['marca'], cleaned['plataforma'], cleaned['cantidad'], cleaned['valor'], d, m, a)
		except Exception as e:
			print(f'exc en coco ==={e}')
			self.date_error()
			return

		#guardar datos
		insert_venta(vent)

		#vaciar entradas en la interfaz
		self.marca.clear()
		self.plataforma.clear()
		self.cantidad.clear()
		self.valor.clear()
		
		#actualiza la tabla que ve el usuario con la nueva entrada creada
		self.actualizar()

	def delete(self):
		row = self.tabla.currentItem().row()
		item = self.tabla.item(row, 0).text()
		delete_venta(item)
		self.actualizar(signal=False)

		
	


app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())