import json


class ArchivoServicio:

    @staticmethod
    def cargar(ruta):

        with open(
            ruta,
            "r",
            encoding="utf-8"
        ) as archivo:

            return json.load(archivo)

    @staticmethod
    def guardar(ruta, datos):

        with open(
            ruta,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )