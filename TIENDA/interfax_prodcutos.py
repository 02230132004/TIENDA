from tkinter import *
from entidad_productos import Producto  # Asegúrate de importar la clase Producto

class InterfazProductos:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Productos")

        self.nombre_var = StringVar()
        self.precio_var = DoubleVar()
        self.stock_var = IntVar()
        self.categoria_var = StringVar()

        # Etiquetas y campos para ingresar datos
        Label(root, text="Nombre:").pack()
        Entry(root, textvariable=self.nombre_var).pack()

        Label(root, text="Precio:").pack()
        Entry(root, textvariable=self.precio_var).pack()

        Label(root, text="Stock:").pack()
        Entry(root, textvariable=self.stock_var).pack()

        Label(root, text="Categoría:").pack()
        Entry(root, textvariable=self.categoria_var).pack()

        # Botón para agregar producto
        Button(root, text="Agregar Producto", command=self.agregar_producto).pack()

    def agregar_producto(self):
        producto = Producto(
            self.nombre_var.get(),
            self.precio_var.get(),
            self.stock_var.get(),
            self.categoria_var.get()
        )
        producto.agregar_producto()
        print("Producto agregado exitosamente.")
