# Restaurante App — Semana 11

## Estudiante
FRANK MARLON CARRIEL SANTOS

## Descripción
Sistema de gestión de productos, usuarios y ventas con persistencia en archivos JSON.

## Estructura
- `datos/` → Archivos JSON generados automáticamente
- `modelos/` → Clases: Producto, Usuario, Venta
- `servicios/` → Lógica de negocio y lectura/escritura JSON
- `main.py` → Menú e interacción por consola

## Ejecución
```bash

python main.py
Restaurante_app_semana11/
├── 📂 datos/ (vacía)
├── 📂 modelos/
│ ├── init.py
│ ├── producto.py
│ ├── usuario.py
│ └── venta.py
├── 📂 servicios/
│ ├── init.py
│ ├── archivo_servicio.py
│ └── restaurante.py
├── main.py
└── README.md
Uso del sistema

Al ejecutar el programa aparecerá un menú con las siguientes opciones:

1. Registrar producto → Ingresa código, nombre, precio y stock

2. Registrar usuario → Ingresa identificación, nombre y correo

3. Listar productos → Muestra todos los productos registrados

4. Realizar venta → Selecciona usuario, producto y cantidad

5. Consultar ventas de un usuario → Muestra el historial de compras

6. Salir → Cierra el programa

Notas

* Los datos se guardan automáticamente en la carpeta datos/

* Si la carpeta datos/ no existe, se crea automáticamente

* Al volver a ejecutar el programa, los datos se cargan automáticamente