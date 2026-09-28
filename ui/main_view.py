import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from modelos.producto import Producto

# Construcción de la ruta base hacia la raíz del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_ASSETS = os.path.join(BASE_DIR, "assets")

class MainView(tk.Frame):
    def __init__(self, master, servicio, cerrar_sesion):
        super().__init__(master)
        self.servicio = servicio
        self.cerrar_sesion_callback = cerrar_sesion
        self.pack(fill="both", expand=True)

        self.crear_encabezado()
        
        # Pestañas principales
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=5)

        # Tab 1: Gestión de Productos
        self.tab_productos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_productos, text="Gestión de Productos")
        self.crear_seccion_productos(self.tab_productos)

        # Tab 2: Usuarios Registrados
        self.tab_usuarios = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_usuarios, text="Usuarios")
        self.crear_seccion_usuarios(self.tab_usuarios)

        # Tab 3: Registro de Ventas (Semana 15)
        self.tab_ventas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_ventas, text="Registro de Ventas")
        self.crear_seccion_ventas(self.tab_ventas)

        # Cargar datos iniciales
        self.cargar_productos()
        self.cargar_ventas()

    # ==========================================
    # ENCABEZADO CON ASSETS (LOGO)
    # ==========================================
    def crear_encabezado(self):
        header_frame = tk.Frame(self, bg="#2C3E50", pady=10)
        header_frame.pack(fill="x")

        # Carga dinámica del logo desde la carpeta assets/
        ruta_logo = os.path.join(RUTA_ASSETS, "logo.png")
        if os.path.exists(ruta_logo):
            try:
                img_pil = Image.open(ruta_logo).resize((38, 38))
                self.logo_img = ImageTk.PhotoImage(img_pil)
                lbl_logo = tk.Label(header_frame, image=self.logo_img, bg="#2C3E50")
                lbl_logo.pack(side=tk.LEFT, padx=15)
            except Exception as e:
                print(f"Error al cargar logo.png: {e}")

        lbl_titulo = tk.Label(
            header_frame, 
            text="SISTEMA DE GESTIÓN DE RESTAURANTE", 
            font=("Arial", 14, "bold"), 
            fg="white", 
            bg="#2C3E50"
        )
        lbl_titulo.pack(side=tk.LEFT)

        btn_salir = tk.Button(
            header_frame, 
            text="Cerrar Sesión", 
            bg="#E74C3C", 
            fg="white", 
            font=("Arial", 9, "bold"),
            command=self.cerrar_sesion_callback
        )
        btn_salir.pack(side=tk.RIGHT, padx=15)

    # ==========================================
    # SECCIÓN: PRODUCTOS
    # ==========================================
    def crear_seccion_productos(self, parent):
        frame_form = tk.LabelFrame(parent, text="Formulario de Producto", padx=10, pady=10)
        frame_form.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_form, text="Código:").grid(row=0, column=0, padx=5, pady=5)
        self.codigo_entry = tk.Entry(frame_form)
        self.codigo_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
        self.nombre_entry = tk.Entry(frame_form)
        self.nombre_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Categoría:").grid(row=2, column=0, padx=5, pady=5)
        self.categoria_entry = tk.Entry(frame_form)
        self.categoria_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Precio:").grid(row=3, column=0, padx=5, pady=5)
        self.precio_entry = tk.Entry(frame_form)
        self.precio_entry.grid(row=3, column=1, padx=5, pady=5)

        frame_btn = tk.Frame(frame_form)
        frame_btn.grid(row=4, column=0, columnspan=2, pady=10)

        tk.Button(frame_btn, text="Registrar", command=self.registrar_producto).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Buscar", command=self.buscar_producto).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Actualizar", command=self.actualizar_producto).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Eliminar", command=self.eliminar_producto).pack(side=tk.LEFT, padx=5)

        frame_tabla = tk.LabelFrame(parent, text="Listado de Productos")
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=5)

        self.tabla_prod = ttk.Treeview(frame_tabla, columns=("codigo", "nombre", "categoria", "precio"), show="headings")
        self.tabla_prod.heading("codigo", text="Código")
        self.tabla_prod.heading("nombre", text="Nombre")
        self.tabla_prod.heading("categoria", text="Categoría")
        self.tabla_prod.heading("precio", text="Precio ($)")
        self.tabla_prod.pack(fill="both", expand=True)

    # ==========================================
    # SECCIÓN: USUARIOS
    # ==========================================
    def crear_seccion_usuarios(self, parent):
        frame_u = tk.LabelFrame(parent, text="Usuarios Registrados en el Sistema", padx=10, pady=10)
        frame_u.pack(fill="both", expand=True, padx=10, pady=10)

        self.lista_usuarios = tk.Listbox(frame_u)
        self.lista_usuarios.pack(fill="both", expand=True)

        for usuario in self.servicio.obtener_usuarios():
            self.lista_usuarios.insert(tk.END, f"Usuario: {usuario.usuario} | Nombre: {usuario.nombre}")

    # ==========================================
    # SECCIÓN: VENTAS (SEMANA 15 - MANEJO DE EVENTOS)
    # ==========================================
    def crear_seccion_ventas(self, parent):
        frame_form_v = tk.LabelFrame(parent, text="Registrar Nueva Venta", padx=10, pady=10)
        frame_form_v.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_form_v, text="Seleccionar Usuario:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.combo_usuarios = ttk.Combobox(frame_form_v, state="readonly", width=30)
        self.combo_usuarios.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form_v, text="Seleccionar Producto:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.combo_productos = ttk.Combobox(frame_form_v, state="readonly", width=30)
        self.combo_productos.grid(row=1, column=1, padx=5, pady=5)

        self.actualizar_combos_ventas()

        # Carga del ícono para el botón de registrar venta
        ruta_icono = os.path.join(RUTA_ASSETS, "icon_sale.png")
        if os.path.exists(ruta_icono):
            try:
                img_ico_pil = Image.open(ruta_icono).resize((18, 18))
                self.ico_sale = ImageTk.PhotoImage(img_ico_pil)
                btn_registrar_venta = tk.Button(
                    frame_form_v,
                    text=" Registrar Venta",
                    image=self.ico_sale,
                    compound="left",
                    bg="#27AE60",
                    fg="white",
                    font=("Arial", 10, "bold"),
                    command=self._on_registrar_venta_click  # <--- Evento: command= + Callback
                )
            except Exception:
                btn_registrar_venta = tk.Button(
                    frame_form_v,
                    text="Registrar Venta",
                    bg="#27AE60",
                    fg="white",
                    font=("Arial", 10, "bold"),
                    command=self._on_registrar_venta_click
                )
        else:
            btn_registrar_venta = tk.Button(
                frame_form_v,
                text="Registrar Venta",
                bg="#27AE60",
                fg="white",
                font=("Arial", 10, "bold"),
                command=self._on_registrar_venta_click
            )
        
        btn_registrar_venta.grid(row=2, column=0, columnspan=2, pady=10)

        # Tabla de Historial de Ventas
        frame_tabla_v = tk.LabelFrame(parent, text="Historial de Ventas Registradas")
        frame_tabla_v.pack(fill="both", expand=True, padx=10, pady=5)

        self.tabla_ventas = ttk.Treeview(frame_tabla_v, columns=("id", "usuario", "producto", "fecha"), show="headings")
        self.tabla_ventas.heading("id", text="ID Venta")
        self.tabla_ventas.heading("usuario", text="Usuario")
        self.tabla_ventas.heading("producto", text="Código Producto")
        self.tabla_ventas.heading("fecha", text="Fecha / Hora")
        self.tabla_ventas.pack(fill="both", expand=True)

    def actualizar_combos_ventas(self):
        usuarios = [u.usuario for u in self.servicio.obtener_usuarios()]
        productos = [p.codigo for p in self.servicio.obtener_productos()]
        
        self.combo_usuarios['values'] = usuarios
        self.combo_productos['values'] = productos

        if usuarios:
            self.combo_usuarios.current(0)
        if productos:
            self.combo_productos.current(0)

    # --- CALLBACK DEL MANEJO DE EVENTOS ---
    def _on_registrar_venta_click(self):
        """
        Callback que responde al clic en el botón.
        Flujo: Acción -> command= -> Callback -> Servicio -> JSON -> Actualizar Vista
        """
        id_usuario = self.combo_usuarios.get()
        codigo_producto = self.combo_productos.get()

        exito, mensaje = self.servicio.registrar_venta(id_usuario, codigo_producto)

        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.cargar_ventas()
        else:
            messagebox.showwarning("Atención", mensaje)

    def cargar_ventas(self):
        for item in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(item)
        for v in self.servicio.obtener_ventas():
            self.tabla_ventas.insert("", tk.END, values=(v.id_venta, v.usuario, v.producto_codigo, v.fecha))

    # --- MÉTODOS DE PRODUCTOS ---
    def cargar_productos(self):
        for item in self.tabla_prod.get_children():
            self.tabla_prod.delete(item)
        for producto in self.servicio.obtener_productos():
            self.tabla_prod.insert("", tk.END, values=(producto.codigo, producto.nombre, producto.categoria, producto.precio))

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
            self.actualizar_combos_ventas()
            messagebox.showinfo("Éxito", "Producto registrado correctamente")
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def buscar_producto(self):
        codigo = self.codigo_entry.get()
        producto = self.servicio.buscar_producto(codigo)
        if producto:
            self.nombre_entry.delete(0, tk.END)
            self.nombre_entry.insert(0, producto.nombre)
            self.categoria_entry.delete(0, tk.END)
            self.categoria_entry.insert(0, producto.categoria)
            self.precio_entry.delete(0, tk.END)
            self.precio_entry.insert(0, producto.precio)
        else:
            messagebox.showwarning("Aviso", "Producto no encontrado")

    def actualizar_producto(self):
        try:
            actualizado = self.servicio.actualizar_producto(
                self.codigo_entry.get(),
                self.nombre_entry.get(),
                self.categoria_entry.get(),
                float(self.precio_entry.get())
            )
            if actualizado:
                self.cargar_productos()
                messagebox.showinfo("Éxito", "Producto actualizado correctamente")
            else:
                messagebox.showwarning("Aviso", "Producto no encontrado")
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def eliminar_producto(self):
        eliminado = self.servicio.eliminar_producto(self.codigo_entry.get())
        if eliminado:
            self.cargar_productos()
            self.actualizar_combos_ventas()
            messagebox.showinfo("Éxito", "Producto eliminado correctamente")
        else:
            messagebox.showwarning("Aviso", "Producto no encontrado")