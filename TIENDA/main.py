from interfaz_clientes import InterfazCliente  # Asegúrate de importar la clase de la interfaz
import tkinter as tk

def main():
    # Crear la ventana principal de Tkinter
    root = tk.Tk()
    # Crear la interfaz de clientes
    interfaz = InterfazCliente(root)
    # Iniciar el loop de la interfaz
    root.mainloop()

if __name__ == "__main__":
    main()
