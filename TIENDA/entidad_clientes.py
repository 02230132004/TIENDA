import mysql.connector

class Cliente:
    def __init__(self, nombre, apellidos, email, historial_compras=0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.historial_compras = historial_compras

    # Método para agregar un cliente
    def agregar_cliente(self):
        conn = mysql.connector.connect(
            host="localhost",
            database="nombre_base",  # Cambia esto con tu base de datos
            user="tu_usuario",       # Cambia esto con tu usuario de MySQL
            password="tu_contraseña" # Cambia esto con tu contraseña de MySQL
        )
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO clientes (nombre, apellidos, email, historial_compras)
        VALUES (%s, %s, %s, %s)
        """, (self.nombre, self.apellidos, self.email, self.historial_compras))
        conn.commit()
        conn.close()

    # Método para obtener todos los clientes
    @staticmethod
    def obtener_clientes():
        conn = mysql.connector.connect(
            host="localhost",
            database="nombre_base",  # Cambia esto con tu base de datos
            user="tu_usuario",       # Cambia esto con tu usuario de MySQL
            password="tu_contraseña" # Cambia esto con tu contraseña de MySQL
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        conn.close()
        return clientes
