import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from modelos.producto import Producto


class MainView(tk.Frame):

    def __init__(
        self,
        master,
        servicio,
        cerrar_sesion
    ):

        super().__init__(master)

        self.servicio = servicio

        self.pack(
            fill="both",
            expand=True
        )

        titulo = tk.Label(
            self,
            text="RESTAURANTE APP",
            font=("Arial", 16, "bold")
        )

        titulo.pack(pady=10)

        self.crear_formulario()

        self.crear_tabla()

        self.crear_usuarios()

        self.crear_botones(cerrar_sesion)

        self.cargar_productos()

    # ==========================
    # FORMULARIO PRODUCTOS
    # ==========================

    def crear_formulario(self):

        formulario = tk.LabelFrame(
            self,
            text="Gestión de Productos",
            padx=10,
            pady=10
        )

        formulario.pack(
            fill="x",
            padx=10,
            pady=10
        )

        tk.Label(
            formulario,
            text="Código:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.codigo_entry = tk.Entry(formulario)

        self.codigo_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        self.nombre_entry = tk.Entry(formulario)

        self.nombre_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Categoría:"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=5
        )

        self.categoria_entry = tk.Entry(formulario)

        self.categoria_entry.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Precio:"
        ).grid(
            row=3,
            column=0,
            padx=5,
            pady=5
        )

        self.precio_entry = tk.Entry(formulario)

        self.precio_entry.grid(
            row=3,
            column=1,
            padx=5,
            pady=5
        )

    # ==========================
    # TABLA PRODUCTOS
    # ==========================

    def crear_tabla(self):

        tabla_frame = tk.LabelFrame(
            self,
            text="Productos Registrados"
        )

        tabla_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        columnas = (
            "codigo",
            "nombre",
            "categoria",
            "precio"
        )

        self.tabla = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tabla.heading(
            "codigo",
            text="Código"
        )

        self.tabla.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla.heading(
            "categoria",
            text="Categoría"
        )

        self.tabla.heading(
            "precio",
            text="Precio"
        )

        self.tabla.pack(
            fill="both",
            expand=True
        )

    # ==========================
    # USUARIOS
    # ==========================

    def crear_usuarios(self):

        usuarios_frame = tk.LabelFrame(
            self,
            text="Usuarios Registrados"
        )

        usuarios_frame.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.lista_usuarios = tk.Listbox(
            usuarios_frame,
            height=4
        )

        self.lista_usuarios.pack(
            fill="x",
            padx=5,
            pady=5
        )

        for usuario in self.servicio.obtener_usuarios():

            self.lista_usuarios.insert(
                tk.END,
                usuario.nombre
            )

    # ==========================
    # BOTONES
    # ==========================

    def crear_botones(
        self,
        cerrar_sesion
    ):

        botones_frame = tk.Frame(self)

        botones_frame.pack(
            pady=10
        )

        tk.Button(
            botones_frame,
            text="Registrar",
            command=self.registrar_producto
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        tk.Button(
            botones_frame,
            text="Buscar",
            command=self.buscar_producto
        ).grid(
            row=0,
            column=1,
            padx=5
        )

        tk.Button(
            botones_frame,
            text="Actualizar",
            command=self.actualizar_producto
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        tk.Button(
            botones_frame,
            text="Eliminar",
            command=self.eliminar_producto
        ).grid(
            row=0,
            column=3,
            padx=5
        )

        tk.Button(
            botones_frame,
            text="Cerrar Sesión",
            command=cerrar_sesion
        ).grid(
            row=0,
            column=4,
            padx=10
        )

    # ==========================
    # ACTUALIZAR TABLA
    # ==========================

    def cargar_productos(self):

        for item in self.tabla.get_children():

            self.tabla.delete(item)

        for producto in self.servicio.obtener_productos():

            self.tabla.insert(
                "",
                tk.END,
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    producto.precio
                )
            )

    # ==========================
    # REGISTRAR
    # ==========================

    def registrar_producto(self):

        try:

            producto = Producto(
                self.codigo_entry.get(),
                self.nombre_entry.get(),
                self.categoria_entry.get(),
                float(self.precio_entry.get())
            )

            self.servicio.registrar_producto(producto)

            self.cargar_productos()

            messagebox.showinfo(
                "Éxito",
                "Producto registrado"
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ==========================
    # BUSCAR
    # ==========================

    def buscar_producto(self):

        codigo = self.codigo_entry.get()

        producto = self.servicio.buscar_producto(
            codigo
        )

        if producto:

            self.nombre_entry.delete(
                0,
                tk.END
            )

            self.nombre_entry.insert(
                0,
                producto.nombre
            )

            self.categoria_entry.delete(
                0,
                tk.END
            )

            self.categoria_entry.insert(
                0,
                producto.categoria
            )

            self.precio_entry.delete(
                0,
                tk.END
            )

            self.precio_entry.insert(
                0,
                producto.precio
            )

        else:

            messagebox.showwarning(
                "Aviso",
                "Producto no encontrado"
            )

    # ==========================
    # ACTUALIZAR
    # ==========================

    def actualizar_producto(self):

        actualizado = self.servicio.actualizar_producto(
            self.codigo_entry.get(),
            self.nombre_entry.get(),
            self.categoria_entry.get(),
            float(self.precio_entry.get())
        )

        if actualizado:

            self.cargar_productos()

            messagebox.showinfo(
                "Éxito",
                "Producto actualizado"
            )

        else:

            messagebox.showwarning(
                "Aviso",
                "Producto no encontrado"
            )

    # ==========================
    # ELIMINAR
    # ==========================

    def eliminar_producto(self):

        eliminado = self.servicio.eliminar_producto(
            self.codigo_entry.get()
        )

        if eliminado:

            self.cargar_productos()

            messagebox.showinfo(
                "Éxito",
                "Producto eliminado"
            )

        else:

            messagebox.showwarning(
                "Aviso",
                "Producto no encontrado"
            )