import os
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

# 1. Definimos la carpeta raíz del proyecto (un nivel arriba de 'servicios')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 2. Construimos las rutas absolutas hacia la carpeta 'datos'
RUTA_PRODUCTOS = os.path.join(BASE_DIR, "datos", "productos.json")
RUTA_USUARIOS = os.path.join(BASE_DIR, "datos", "usuarios.json")


class RestauranteServicio:

    def __init__(self):

        # Usamos RUTA_PRODUCTOS y RUTA_USUARIOS en lugar de "datos/..."
        datos_productos = ArchivoServicio.cargar(RUTA_PRODUCTOS)

        datos_usuarios = ArchivoServicio.cargar(RUTA_USUARIOS)

        self.productos = [
            Producto.desde_diccionario(p)
            for p in datos_productos
        ]

        self.usuarios = [
            Usuario.desde_diccionario(u)
            for u in datos_usuarios
        ]

    def validar_login(
        self,
        usuario,
        contrasena
    ):

        for u in self.usuarios:

            if (
                u.usuario == usuario
                and
                u.contrasena == contrasena
            ):
                return True

        return False

    def obtener_productos(self):
        return self.productos

    def obtener_usuarios(self):
        return self.usuarios

    def guardar_productos(self):

        # También usamos RUTA_PRODUCTOS aquí para guardar
        ArchivoServicio.guardar(
            RUTA_PRODUCTOS,
            [
                p.convertir_a_diccionario()
                for p in self.productos
            ]
        )

    def registrar_producto(self, producto):

        self.productos.append(producto)

        self.guardar_productos()

    def buscar_producto(self, codigo):

        for producto in self.productos:

            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo,
        nombre,
        categoria,
        precio
    ):

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