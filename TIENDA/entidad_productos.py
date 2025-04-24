import mysql.connector

class Producto:
    def __init__(self, nombre, precio, stock, categoria):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    # Método para agregar un producto
    def agregar_producto(self):
        conn = mysql.connector.connect(
            host="localhost",
            database="nombre_base",  # Cambia esto con tu base de datos
            user="tu_usuario",       # Cambia esto con tu usuario de MySQL
            password="tu_contraseña" # Cambia esto con tu contraseña de MySQL
        )
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO productos (nombre, precio, stock, categoria)
        VALUES (%s, %s, %s, %s)
        """, (self.nombre, self.precio, self.stock, self.categoria))
        conn.commit()
        conn.close()

    # Método para obtener todos los productos
    @staticmethod
    def obtener_productos():
        conn = mysql.connector.connect(
            host="localhost",
            database="nombre_base",  # Cambia esto con tu base de datos
            user="tu_usuario",       # Cambia esto con tu usuario de MySQL
            password="tu_contraseña" # Cambia esto con tu contraseña de MySQL
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        conn.close()
        return productos
