# 🍽️ Restaurante App — Semana 11

## Estudiante
FRANK MARLON CARRIEL SANTOS

## Descripción del sistema
Sistema de administración de productos, usuarios y ventas para un restaurante. Permite registrar productos con stock, registrar usuarios, realizar ventas que relacionen usuarios y productos, controlar el stock disponible, consultar el historial de compras de un usuario y conservar toda la información mediante persistencia en archivos JSON.

## Estructura del proyecto
Restaurante_app_semana11/
├── datos/
│ ├── productos.json ← Se genera automáticamente
│ ├── usuarios.json ← Se genera automáticamente
│ └── ventas.json ← Se genera automáticamente
├── modelos/
│ ├── init.py
│ ├── producto.py ← Entidad Producto con control de stock
│ ├── usuario.py ← Entidad Usuario
│ └── venta.py ← Entidad Venta (relación Usuario–Producto)
├── servicios/
│ ├── init.py
│ ├── archivo_servicio.py ← Lectura y escritura de los 3 archivos JSON
│ └── restaurante.py ← Lógica de negocio, colecciones y reglas
├── main.py ← Menú e interacción por consola
└── README.md ← Documentación

## Funcionamiento del Stock
Cada producto maneja una cantidad disponible (`stock`). Al realizar una venta, el sistema valida:
- Que la cantidad solicitada sea mayor a cero
- Que exista stock suficiente
- Si la venta es válida → se resta automáticamente del stock
- El stock nunca puede ser negativo

## Relación Usuario — Producto mediante Venta
Una venta representa la relación entre:
- **Usuario**: quien realiza la compra (por su identificación)
- **Producto**: lo que se compra (por su ID)
- **Cantidad**: unidades adquiridas

### Flujo de una venta:
1. Se verifica que el usuario exista
2. Se verifica que el producto exista
3. Se valida cantidad mayor a cero
4. Se comprueba stock suficiente
5. ✅ Si todo es válido → se crea la Venta → se resta stock → se guardan cambios

## Persistencia de datos
El sistema guarda automáticamente:
- **productos.json** → después de agregar producto o realizar venta
- **usuarios.json** → después de registrar un usuario
- **ventas.json** → después de cada venta realizada

Al iniciar el programa se leen los tres archivos y se reconstruyen automáticamente los objetos.

## Excepciones controladas
| Excepción | Situación | Respuesta |
|---|---|---|
| `FileNotFoundError` | Archivo aún no creado | ✅ Inicia con lista vacía |
| `json.JSONDecodeError` | Archivo corrupto o inválido | ⚠️ Avisa e inicia vacío |
| `PermissionError` | Sin permisos de lectura/escritura | ❌ Muestra mensaje y continúa |
| `KeyError` | Registro incompleto | ⚠️ Omite solo ese registro |
| `ValueError` | Datos inválidos (precio, cantidad) | ⚠️ Rechaza la operación |

## Ejecución del programa
```bash
python main.py