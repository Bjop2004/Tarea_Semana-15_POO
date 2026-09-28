import os
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RUTA_PRODUCTOS = os.path.join(BASE_DIR, "datos", "productos.json")
RUTA_USUARIOS = os.path.join(BASE_DIR, "datos", "usuarios.json")
RUTA_VENTAS = os.path.join(BASE_DIR, "datos", "ventas.json")

class RestauranteServicio:
    def __init__(self):
        # Cargar datos existentes usando ArchivoServicio
        datos_productos = ArchivoServicio.cargar(RUTA_PRODUCTOS) if os.path.exists(RUTA_PRODUCTOS) else []
        datos_usuarios = ArchivoServicio.cargar(RUTA_USUARIOS) if os.path.exists(RUTA_USUARIOS) else []
        datos_ventas = ArchivoServicio.cargar(RUTA_VENTAS) if os.path.exists(RUTA_VENTAS) else []

        self.productos = [Producto.desde_diccionario(p) for p in datos_productos]
        self.usuarios = [Usuario.desde_diccionario(u) for u in datos_usuarios]
        self.ventas = [Venta.desde_diccionario(v) for v in datos_ventas]

    # ==========================
    # LOGIN / AUTENTICACIÓN
    # ==========================
    def validar_login(self, usuario, contrasena):
        for u in self.usuarios:
            # Compara coincidencia exacta de usuario y contraseña
            if u.usuario.strip() == usuario.strip() and u.contrasena.strip() == contrasena.strip():
                return True
        return False

    # ==========================
    # GESTIÓN DE PRODUCTOS
    # ==========================
    def obtener_productos(self):
        return self.productos

    def guardar_productos(self):
        ArchivoServicio.guardar(
            RUTA_PRODUCTOS,
            [p.convertir_a_diccionario() for p in self.productos]
        )

    def registrar_producto(self, producto):
        self.productos.append(producto)
        self.guardar_productos()

    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_producto(self, codigo, nombre, categoria, precio):
        producto = self.buscar_producto(codigo)
        if producto:
            producto.nombre = nombre
            producto.categoria = categoria
            producto.precio = precio
            self.guardar_productos()
            return True
        return False

    def eliminar_producto(self, codigo):
        producto = self.buscar_producto(codigo)
        if producto:
            self.productos.remove(producto)
            self.guardar_productos()
            return True
        return False

    # ==========================
    # GESTIÓN DE USUARIOS
    # ==========================
    def obtener_usuarios(self):
        return self.usuarios

    # ==========================
    # GESTIÓN DE VENTAS (Semana 15)
    # ==========================
    def obtener_ventas(self):
        return self.ventas

    def guardar_ventas(self):
        ArchivoServicio.guardar(
            RUTA_VENTAS,
            [v.convertir_a_diccionario() for v in self.ventas]
        )

    def registrar_venta(self, usuario_id: str, codigo_producto: str) -> tuple[bool, str]:
        if not usuario_id or not codigo_producto:
            return False, "Debe seleccionar un usuario y un producto válidos."

        usuario_existe = any(u.usuario == usuario_id for u in self.usuarios)
        producto_existe = any(p.codigo == codigo_producto for p in self.productos)

        if not usuario_existe:
            return False, "El usuario seleccionado no existe."
        if not producto_existe:
            return False, "El producto seleccionado no existe."

        nuevo_id = f"V-{len(self.ventas) + 1:04d}"
        nueva_venta = Venta(id_venta=nuevo_id, usuario=usuario_id, producto_codigo=codigo_producto)
        
        self.ventas.append(nueva_venta)
        self.guardar_ventas()
        return True, f"Venta {nuevo_id} registrada con éxito."