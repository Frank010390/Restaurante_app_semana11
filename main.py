import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n" + "=" * 40)
    print("      RESTAURANTE APP — Semana 11")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Registrar usuario")
    print("3. Listar productos")
    print("4. Realizar venta")
    print("5. Consultar ventas de un usuario")
    print("6. Salir")
    print("-" * 40)

def main():
    restaurante = Restaurante()
    restaurante.iniciar()
    print("✅ Datos cargados correctamente")

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            codigo = input("Código del producto: ").strip()
            nombre = input("Nombre del producto: ").strip()
            try:
                precio = float(input("Precio: ").strip())
                stock = int(input("Cantidad en stock: ").strip())
                if restaurante.registrar_producto(Producto(codigo, nombre, precio, stock)):
                    print("✅ Producto registrado")
                else:
                    print("❌ El producto ya existe")
            except ValueError as e:
                print(f"❌ Datos inválidos: {e}")

        elif opcion == "2":
            ide = input("Identificación: ").strip()
            nombre = input("Nombre: ").strip()
            correo = input("Correo: ").strip()
            if restaurante.registrar_usuario(Usuario(ide, nombre, correo)):
                print("✅ Usuario registrado")
            else:
                print("❌ Ya existe un usuario con esa identificación")

        elif opcion == "3":
            productos = restaurante.listar_productos()
            if not productos:
                print("📋 Sin productos registrados")
                continue
            print("\n--- Lista de Productos ---")
            for p in productos:
                print(f"📦 {p.codigo} | {p.nombre} | ${p.precio:.2f} | Stock: {p.stock}")

        elif opcion == "4":
            ide_usuario = input("Identificación del usuario: ").strip()
            cod_producto = input("Código del producto: ").strip()
            try:
                cantidad = int(input("Cantidad a comprar: ").strip())
            except ValueError:
                print("❌ Debe ingresar un número válido")
                continue
            exito, mensaje = restaurante.vender_producto(cod_producto, ide_usuario, cantidad)
            print(mensaje)

        elif opcion == "5":
            ide_usuario = input("Identificación del usuario: ").strip()
            ventas = restaurante.consultar_ventas_por_usuario(ide_usuario)
            if not ventas:
                print("📋 El usuario no tiene compras registradas")
                continue
            print(f"\n--- Compras del usuario {ide_usuario} ---")
            for venta, prod in ventas:
                nom_prod = prod.nombre if prod else "Producto desconocido"
                print(f"📦 {venta.producto_codigo} - {nom_prod} | Cantidad: {venta.cantidad}")

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción no válida")

if __name__ == "__main__":
    main()