# Restaurante App — Semana 14: Componentes y Contenedores

Aplicación de escritorio para la gestión de un restaurante desarrollada en Python con Tkinter. En esta versión de la **Semana 14**, el proyecto evoluciona hacia una experiencia de usuario más organizada, amigable y modular mediante la implementación formal de **componentes, contenedores (frames) y gestores de geometría**, manteniendo la arquitectura en capas y la persistencia en archivos JSON.

---

## 📌 Propósito de la Semana 14

El objetivo principal de esta entrega es refactorizar y mejorar la capa de interfaz de usuario (`ui`) aplicando principios de diseño de interfaces gráficas (GUI):
* **Jerarquía visual sólida:** Uso de contenedores (`tk.Frame`, `ttk.LabelFrame`) para separar la navegación, los formularios de captura y los paneles de visualización.
* **Separación de responsabilidades:** Mantener la lógica de negocio y validaciones estrictamente dentro de los servicios (`RestauranteServicio`) y la persistencia en archivos JSON (`ArchivoServicio`), evitando colocar lógica dentro de la vista.
* **Operaciones CRUD sobre Productos:** Permitir el registro, consulta/carga, actualización y eliminación de productos desde la GUI mediante controles interactivos y acciones de botones (`command=`).

---

## 📁 Estructura del Proyecto

El repositorio mantiene la arquitectura de software en capas estructurada de la siguiente manera:

```text
restaurante_app/
├── datos/
│   ├── productos.json          # Persistencia de productos
│   └── usuarios.json           # Persistencia de usuarios
├── modelos/
│   ├── __init__.py
│   ├── producto.py             # Modelo de entidad Producto
│   └── usuario.py              # Modelo de entidad Usuario
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py     # Manejo genérico de lectura/escritura JSON
│   └── restaurante_servicio.py # Lógica de negocio y validaciones
├── ui/
│   ├── __init__.py
│   ├── login_view.py           # Vista de inicio de sesión
│   └── main_view.py            # Vista principal (Contenedores y Componentes)
├── main.py                     # Punto de entrada de la aplicación
└── README.md                   # Documentación del proyecto