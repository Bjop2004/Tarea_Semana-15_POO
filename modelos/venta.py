from datetime import datetime

class Venta:
    def __init__(self, id_venta: str, usuario: str, producto_codigo: str, fecha: str = None):
        self.id_venta = id_venta
        self.usuario = usuario
        self.producto_codigo = producto_codigo
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def convertir_a_diccionario(self) -> dict:
        return {
            "id_venta": self.id_venta,
            "usuario": self.usuario,
            "producto_codigo": self.producto_codigo,
            "fecha": self.fecha
        }

    @staticmethod
    def desde_diccionario(data: dict):
        return Venta(
            id_venta=data["id_venta"],
            usuario=data["usuario"],
            producto_codigo=data["producto_codigo"],
            fecha=data["fecha"]
        )

    def __str__(self):
        return f"{self.id_venta} - {self.usuario} - {self.producto_codigo} ({self.fecha})"