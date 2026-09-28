# Restaurante App — Semana 15: Manejo de Eventos

Aplicación de escritorio para la gestión de un restaurante desarrollada en Python utilizando Tkinter. En esta versión de la **Semana 15**, el proyecto evoluciona incorporando el **manejo de eventos mediante `command=` y *callbacks***, la gestión de la entidad **Venta**, persistencia en archivos JSON y el uso obligatorio de recursos visuales desde la carpeta `assets/`.

---

## 📌 Propósito de la Semana 15

El objetivo principal de esta entrega es aplicar los **conceptos fundamentales del manejo de eventos en GUIs**, demostrando cómo una acción del usuario en la interfaz inicia y coordina una operación sin concentrar la lógica del sistema dentro de la vista.

### **Aspectos Clave:**
* **Asociación de Eventos:** Uso de `command=self._on_registrar_venta_click` para vincular botones a callbacks explícitos sin ejecución inmediata.
* **Desacoplamiento y Arquitectura:** La interfaz (`ui`) no realiza manipulaciones directas sobre los datos. Toda regla de negocio, validación y persistencia es delegada a `RestauranteServicio` y `ArchivoServicio`.
* **Identidad Visual (`assets/`):** Integración de logotipo e íconos dentro de la interfaz para mejorar la experiencia de usuario (UX).

---

## 📁 Estructura del Proyecto

El repositorio mantiene la arquitectura modular en capas:

```text
restaurante_app/
├── assets/
│   ├── logo.png                # Logotipo del restaurante
│   └── icon_sale.png           # Ícono para acciones de venta
├── datos/
│   ├── productos.json          # Persistencia de productos
│   ├── usuarios.json           # Persistencia de usuarios
│   └── ventas.json             # Persistencia de ventas (Semana 15)
├── modelos/
│   ├── __init__.py
│   ├── producto.py             # Modelo de entidad Producto
│   ├── usuario.py              # Modelo de entidad Usuario
│   └── venta.py                # Modelo de entidad Venta (Semana 15)
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py     # Lectura y escritura genérica en JSON
│   └── restaurante_servicio.py # Lógica de negocio y validaciones
├── ui/
│   ├── __init__.py
│   ├── login_view.py           # Vista de inicio de sesión
│   └── main_view.py            # Vista principal (Eventos, Notebook y Vistas)
├── main.py                     # Punto de entrada de la aplicación
└── README.md                   # Documentación técnica

## 🚀 Instrucciones de Ejecución

### **Requisitos Previos**
1. Tener instalado **Python 3.10+**.
2. Instalar la librería externa **Pillow** (utilizada para la carga, redimensionamiento y visualización adecuada de los recursos gráficos `.png` de la carpeta `assets/` dentro de la interfaz gráfica de Tkinter):
   ```bash
   pip install pillow