import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_ASSETS = os.path.join(BASE_DIR, "assets")

class LoginView(tk.Frame):
    def __init__(self, master, servicio, abrir_main):
        super().__init__(master)
        self.servicio = servicio
        self.abrir_main = abrir_main
        self.pack(expand=True)

        ruta_logo = os.path.join(RUTA_ASSETS, "logo.png")
        if os.path.exists(ruta_logo):
            img = Image.open(ruta_logo).resize((80, 80))
            self.logo_img = ImageTk.PhotoImage(img)
            tk.Label(self, image=self.logo_img).pack(pady=10)

        tk.Label(self, text="Inicio de Sesión", font=("Arial", 14, "bold")).pack(pady=5)

        tk.Label(self, text="Usuario").pack()
        self.usuario_entry = tk.Entry(self)
        self.usuario_entry.pack()

        tk.Label(self, text="Contraseña").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Ingresar", bg="#3498DB", fg="white", command=self.ingresar).pack(pady=15)

    def ingresar(self):
        usuario = self.usuario_entry.get()
        password = self.password_entry.get()
        if self.servicio.validar_login(usuario, password):
            self.abrir_main()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")