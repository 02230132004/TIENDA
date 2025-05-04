import mysql.connector

class Producto:
    def __init__(self, id, nombre, precio, stock, categoria):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def guardar(self, conexion):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO productos (id, nombre, precio, stock, categoria) VALUES (%s, %s, %s, %s, %s)",
                       (self.id, self.nombre, self.precio, self.stock, self.categoria))
        conexion.commit()
