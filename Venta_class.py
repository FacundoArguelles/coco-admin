import datetime


class Venta:

	def __init__(self, m, p, c, v, dia, mes, anio):
		self.marca = m
		self.plataforma = p
		self.cantidad = c
		self.valor = v

		try:
			dt = datetime.date(anio, mes, dia)
			self.fecha = dt
			#print(f'fecha==={dt}')
		except Exception as e:
			print(f'exception==={e}')


	def __repr__(self):
		return f'compra {self.id} a: {self.marca}, {self.plataforma} por {self.valor}, el {self.fecha}'

