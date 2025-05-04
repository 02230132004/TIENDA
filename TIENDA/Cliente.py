import mysql.connector

class Cliente:
    def __init__(self, id, nombre, apellidos, email):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

    def guardar(self, conexion):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO clientes (id, nombre, apellidos, email) VALUES (%s, %s, %s, %s)",
                       (self.id, self.nombre, self.apellidos, self.email))
        conexion.commit()


