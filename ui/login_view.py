import tkinter as tk
from tkinter import messagebox


class LoginView(tk.Frame):

    def __init__(
        self,
        master,
        servicio,
        abrir_main
    ):

        super().__init__(master)

        self.servicio = servicio
        self.abrir_main = abrir_main

        self.pack(expand=True)

        tk.Label(
            self,
            text="Usuario"
        ).pack()

        self.usuario_entry = tk.Entry(self)
        self.usuario_entry.pack()

        tk.Label(
            self,
            text="Contraseña"
        ).pack()

        self.password_entry = tk.Entry(
            self,
            show="*"
        )

        self.password_entry.pack()

        tk.Button(
            self,
            text="Ingresar",
            command=self.ingresar
        ).pack(pady=10)

    def ingresar(self):

        usuario = self.usuario_entry.get()

        password = self.password_entry.get()

        if self.servicio.validar_login(
            usuario,
            password
        ):

            self.abrir_main()

        else:

            messagebox.showerror(
                "Error",
                "Credenciales incorrectas"
            )