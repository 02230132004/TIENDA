import tkinter as tk
from tkinter import messagebox
from Cliente import Cliente

class InterfazCliente:
    def __init__(self, root, conexion):
        self.root = root
        self.conexion = conexion
        self.root.title("Gestión de Clientes")

        self.id = tk.Entry(root)
        self.nombre = tk.Entry(root)
        self.apellidos = tk.Entry(root)
        self.email = tk.Entry(root)

        tk.Label(root, text="ID").grid(row=0, column=0)
        self.id.grid(row=0, column=1)
        tk.Label(root, text="Nombre").grid(row=1, column=0)
        self.nombre.grid(row=1, column=1)
        tk.Label(root, text="Apellidos").grid(row=2, column=0)
        self.apellidos.grid(row=2, column=1)
        tk.Label(root, text="Email").grid(row=3, column=0)
        self.email.grid(row=3, column=1)

        tk.Button(root, text="Guardar Cliente", command=self.guardar_cliente).grid(row=4, columnspan=2)

    def guardar_cliente(self):
        try:
            cliente = Cliente(self.id.get(), self.nombre.get(), self.apellidos.get(), self.email.get())
            cliente.guardar(self.conexion)
            messagebox.showinfo("Guardado", "Cliente guardado correctamente")
        except Exception as e:
            messagebox.showerror("Error", str(e))
