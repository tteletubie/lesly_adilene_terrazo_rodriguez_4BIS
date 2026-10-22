import tkinter as tk
from tkinter import ttk, messagebox
from model.products_model import Product


class DashboardVentana:
    def __init__(self, root, nombre_completo):
        self.root = root
        self.root.title("Panel Principal - Sistema")
        self.root.geometry("800x500")
        self.producto_model = Product()

      
        tk.Label(root, text=f"Bienvenido/a, {nombre_completo}",
                 font=("Helvetica", 12, "bold")).pack(pady=10)

        # Pestañas
        self.tabs = ttk.Notebook(root)
        self.tabs.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_inicio = tk.Frame(self.tabs)
        self.tab_inventario = tk.Frame(self.tabs)
        self.tabs.add(self.tab_inicio, text="Inicio")
        self.tabs.add(self.tab_inventario, text="Inventario de Productos")

        self._crear_inicio()
        self._crear_inventario()
        self._cargar_productos()

    def _crear_inicio(self):
        tk.Label(self.tab_inicio, text="Bienvenido al sistema de inventario",
                 font=("Helvetica", 14)).pack(pady=50)

    def _crear_inventario(self):
        
        form = tk.LabelFrame(self.tab_inventario, text="Registrar Producto", padx=10, pady=10)
        form.pack(side="left", fill="y", padx=10, pady=10)

        tk.Label(form, text="Nombre:").pack(anchor="w")
        self.entry_nombre = tk.Entry(form)
        self.entry_nombre.pack(pady=(0, 10))

        tk.Label(form, text="Precio:").pack(anchor="w")
        self.entry_precio = tk.Entry(form)
        self.entry_precio.pack(pady=(0, 10))

        tk.Label(form, text="Stock:").pack(anchor="w")
        self.entry_stock = tk.Entry(form)
        self.entry_stock.pack(pady=(0, 10))

        tk.Button(form, text="Guardar Producto",
                  command=self._guardar_producto).pack(pady=10)

       
        self.tabla = ttk.Treeview(
            self.tab_inventario,
            columns=("id", "nombre", "precio", "stock"),
            show="headings"
        )
        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("precio", text="Precio ($)")
        self.tabla.heading("stock", text="Stock")

        self.tabla.column("id", width=50, anchor="center")
        self.tabla.column("nombre", width=200)
        self.tabla.column("precio", width=100, anchor="e")
        self.tabla.column("stock", width=80, anchor="center")

        self.tabla.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    def _cargar_productos(self):
        
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for producto in self.producto_model.obtener_todos():
            self.tabla.insert("", "end", values=producto)

    def _guardar_producto(self):
        nombre = self.entry_nombre.get().strip()
        precio = self.entry_precio.get().strip()
        stock = self.entry_stock.get().strip()

        if not nombre or not precio or not stock:
            messagebox.showwarning("Campos vacíos", "Llena todos los campos.")
            return

        try:
            precio = float(precio)
            stock = int(stock)
        except ValueError:
            messagebox.showerror("Error", "Precio debe ser número y Stock debe ser entero.")
            return

        self.producto_model.agregar(nombre, precio, stock)
        messagebox.showinfo("Listo", "Producto guardado.")

        self.entry_nombre.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)
        self._cargar_productos()