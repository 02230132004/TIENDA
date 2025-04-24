import tkinter as tk
from tkinter import messagebox
from entidad_clientes import Cliente  # Asegúrate de que la clase Cliente esté importada correctamente

class InterfazCliente:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Clientes")

        # Definir variables de Tkinter
        self.nombre_var = tk.StringVar()
        self.apellidos_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.historial_compras_var = tk.DoubleVar()

        # Etiquetas y campos de entrada para los datos del cliente
        tk.Label(root, text="Nombre:").grid(row=0, column=0)
        self.nombre_entry = tk.Entry(root, textvariable=self.nombre_var)
        self.nombre_entry.grid(row=0, column=1)

        tk.Label(root, text="Apellidos:").grid(row=1, column=0)
        self.apellidos_entry = tk.Entry(root, textvariable=self.apellidos_var)
        self.apellidos_entry.grid(row=1, column=1)

        tk.Label(root, text="Email:").grid(row=2, column=0)
        self.email_entry = tk.Entry(root, textvariable=self.email_var)
        self.email_entry.grid(row=2, column=1)

        tk.Label(root, text="Historial de Compras:").grid(row=3, column=0)
        self.historial_compras_entry = tk.Entry(root, textvariable=self.historial_compras_var)
        self.historial_compras_entry.grid(row=3, column=1)

        # Botón para agregar cliente
        self.agregar_button = tk.Button(root, text="Agregar Cliente", command=self.agregar_cliente)
        self.agregar_button.grid(row=4, column=0, columnspan=2)

        # Botón para mostrar clientes
        self.mostrar_button = tk.Button(root, text="Mostrar Clientes", command=self.mostrar_clientes)
        self.mostrar_button.grid(row=5, column=0, columnspan=2)

        # Área para mostrar los clientes
        self.clientes_listbox = tk.Listbox(root, width=50, height=10)
        self.clientes_listbox.grid(row=6, column=0, columnspan=2)

    def agregar_cliente(self):
        # Obtener los valores de los campos de entrada
        nombre = self.nombre_var.get()
        apellidos = self.apellidos_var.get()
        email = self.email_var.get()
        historial_compras = self.historial_compras_var.get()

        if nombre and apellidos and email:
            # Crear una instancia de Cliente y agregarlo a la base de datos
            cliente = Cliente(nombre, apellidos, email, historial_compras)
            cliente.agregar_cliente()

            # Limpiar los campos después de agregar el cliente
            self.nombre_var.set("")
            self.apellidos_var.set("")
            self.email_var.set("")
            self.historial_compras_var.set(0)

            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", "Cliente agregado correctamente.")
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")

    def mostrar_clientes(self):
        # Limpiar la lista de clientes
        self.clientes_listbox.delete(0, tk.END)

        # Obtener todos los clientes de la base de datos
        clientes = Cliente.obtener_clientes()

        # Mostrar los clientes en el Listbox
        for cliente in clientes:
            self.clientes_listbox.insert(tk.END, f"ID: {cliente[0]}, Nombre: {cliente[1]} {cliente[2]}, Email: {cliente[3]}, Historial de Compras: ${cliente[4]:.2f}")


if __name__ == "__main__":
    root = tk.Tk()
    interfaz = InterfazCliente(root)
    root.mainloop()
