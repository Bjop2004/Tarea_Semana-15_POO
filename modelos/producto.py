class Producto:

    def __init__(self, codigo, nombre, categoria, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    @staticmethod
    def desde_diccionario(data):

        return Producto(
            data["codigo"],
            data["nombre"],
            data["categoria"],
            data["precio"]
        )

    def convertir_a_diccionario(self):

        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }

    def __str__(self):

        return (
            f"{self.codigo} - "
            f"{self.nombre} - "
            f"{self.categoria} - "
            f"${self.precio}"
        )