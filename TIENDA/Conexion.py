import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        password="tu_contraseña",
        database="tienda"
    )
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                        id VARCHAR(10) PRIMARY KEY,
                        nombre VARCHAR(100),
                        precio FLOAT,
                        stock INT,
                        categoria VARCHAR(50))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                        id VARCHAR(10) PRIMARY KEY,
                        nombre VARCHAR(100),
                        apellidos VARCHAR(100),
                        email VARCHAR(100))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS compras (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        id_cliente VARCHAR(10),
                        id_producto VARCHAR(10),
                        valor FLOAT,
                        FOREIGN KEY(id_cliente) REFERENCES clientes(id),
                        FOREIGN KEY(id_producto) REFERENCES productos(id))''')
    conexion.commit()
    return conexion