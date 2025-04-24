import mysql.connector # type: ignore
from mysql.connector import Error # type: ignore

# Función para conectar con MySQL
def conectar():
    try:
        # Conecta a tu base de datos MySQL
        conn = mysql.connector.connect(
            host="localhost",         # El host donde está corriendo MySQL (generalmente localhost)
            database="nombre_base",   # Nombre de la base de datos (cambia esto con tu base de datos)
            user="tu_usuario",        # Tu usuario de MySQL
            password="tu_contraseña"  # Tu contraseña de MySQL
        )
        if conn.is_connected():
            print("Conexión exitosa a la base de datos")
        return conn
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Crear tablas si no existen
def crear_tablas():
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        
        # Crear la tabla de productos
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100),
            precio DECIMAL(10, 2),
            stock INT,
            categoria VARCHAR(100)
        )
        """)

        # Crear la tabla de clientes
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100),
            apellidos VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            historial_compras DECIMAL(10, 2) DEFAULT 0
        )
        """)

        conn.commit()  # Guardar los cambios
        conn.close()   # Cerrar la conexión
