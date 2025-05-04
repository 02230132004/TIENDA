import tkinter as tk
from tkinter import messagebox
from Producto import Producto

class InterfazProducto:
    def __init__(self, root, conexion):
        self.root = root
        self.conexion = conexion
        self.root.title("Gestión de Productos")

        self.id = tk.Entry(root)
        self.nombre = tk.Entry(root)
        self.precio = tk.Entry(root)
        self.stock = tk.Entry(root)
        self.categoria = tk.Entry(root)

        tk.Label(root, text="ID").grid(row=0, column=0)
        self.id.grid(row=0, column=1)
        tk.Label(root, text="Nombre").grid(row=1, column=0)
        self.nombre.grid(row=1, column=1)
        tk.Label(root, text="Precio").grid(row=2, column=0)
        self.precio.grid(row=2, column=1)
        tk.Label(root, text="Stock").grid(row=3, column=0)
        self.stock.grid(row=3, column=1)
        tk.Label(root, text="Categoría").grid(row=4, column=0)
        self.categoria.grid(row=4, column=1)

        tk.Button(root, text="Guardar Producto", command=self.guardar_producto).grid(row=5, columnspan=2)

    def guardar_producto(self):
        try:
            producto = Producto(self.id.get(), self.nombre.get(), float(self.precio.get()), int(self.stock.get()), self.categoria.get())
            producto.guardar(self.conexion)
            messagebox.showinfo("Guardado", "Producto guardado correctamente")
        except Exception as e:
            messagebox.showerror("Error", str(e))