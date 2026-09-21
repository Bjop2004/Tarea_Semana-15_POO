import tkinter as tk

from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class App:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title(
            "Restaurante App"
        )

        self.root.geometry(
            "900x600"
        )

        self.servicio = RestauranteServicio()

        self.frame_actual = None

        self.mostrar_login()

        self.root.mainloop()

    def limpiar(self):

        if self.frame_actual:
            self.frame_actual.destroy()

    def mostrar_login(self):

        self.limpiar()

        self.frame_actual = LoginView(
            self.root,
            self.servicio,
            self.mostrar_main
        )

    def mostrar_main(self):

        self.limpiar()

        self.frame_actual = MainView(
            self.root,
            self.servicio,
            self.mostrar_login
        )


if __name__ == "__main__":

    App()