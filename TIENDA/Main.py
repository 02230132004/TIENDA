import tkinter as tk
from Conexion import conectar
from Interfazproducto import InterfazProducto
from Interfazcliente import InterfazCliente

conexion = conectar()

raiz = tk.Tk()
raiz.title("Sistema de Gestión")

frame = tk.Frame(raiz)
frame.pack()

tk.Button(frame, text="Gestión de Productos", command=lambda: InterfazProducto(tk.Toplevel(raiz), conexion)).pack()
tk.Button(frame, text="Gestión de Clientes", command=lambda: InterfazCliente(tk.Toplevel(raiz), conexion)).pack()

raiz.mainloop()