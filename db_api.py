import sqlite3
import pprint
from Venta_class import Venta


def check_table():
	try:
		conn = sqlite3.connect('ventas.db')
		c = conn.cursor()
		c.execute('''CREATE table IF NOT EXISTS ventas (
						venta_id INTEGER PRIMARY KEY,
						marca text,
						plataforma text,
						cantidad integer,
						valor real,
						fecha text
						)''')
		conn.commit()
		conn.close()
	except Exception as e:
		print(e)

def insert_venta(venta):
	conn = sqlite3.connect('ventas.db')
	c = conn.cursor()
	#Cuando se usa una columna con autoincremento, hay que especificar los campos despues del nombre de la tabla
	c.execute("INSERT INTO ventas(marca, plataforma, cantidad, valor, fecha) VALUES(:marca, :plat, :cant, :val, :fecha)",
					{'marca': venta.marca, 'plat': venta.plataforma, 'cant': venta.cantidad,
					 'val': venta.valor,'fecha': venta.fecha})
	conn.commit()
	conn.close()


def get_all_ventas():
	conn = sqlite3.connect('ventas.db')
	c = conn.cursor()
	c.execute("SELECT * FROM ventas ORDER BY -venta_id")
	all_ = c.fetchall()
	conn.close()
	pprint.pprint(f'ALL_: {all_}')
	if not all_:
		return False
	else:
		return all_


def delete_venta(v_id):
	conn = sqlite3.connect('ventas.db')
	c = conn.cursor()
	c.execute("DELETE FROM ventas WHERE venta_id=:venta_id", {'venta_id':v_id})
	conn.commit()
	conn.close()




# def update_venta(v_id):
# 	conn = sqlite3.connect('data/ventas.db')
# 	c = conn.cursor()
# 	c.execute("UPDATE ventas SET  WHERE venta_id=:venta_id", {'venta_id':v_id})



# create_table()
# v2 = Venta('segunda', 'segunda', 20, 600, 26, 8, 2018)
# insert_venta(v2)
#delete_venta(v1)

# c = connection()
# c.execute('SELECT * FROM ventas')

# for r in c.fetchall():
# 	print(r)	





