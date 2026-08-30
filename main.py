from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


def mostrar_menu():
    print("\n" + "=" * 50)
    print("          🍽️  RESTAURANTE APP — SEMANA 11")
    print("=" * 50)
    print("1. Registrar producto")
    print("2. Registrar usuario")
    print("3. Listar productos")
    print("4. Listar usuarios")
    print("5. Realizar venta")
    print("6. Consultar ventas de un usuario")
    print("7. Salir")
    print("=" * 50)


def main():
    restaurante = Restaurante()
    restaurante.cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-7): ")

        if opcion == "1":
            print("\n--- Registrar Producto ---")
            try:
                id_p = int(input("ID del producto: "))
                nombre = input("Nombre: ")
                precio = float(input("Precio: $"))
                categoria = input("Categoría: ")
                stock = int(input("Cantidad en stock: "))
                prod = Producto(id_p, nombre, precio, categoria, stock)
                restaurante.agregar_producto(prod)
            except ValueError:
                print("❌ Datos inválidos, intenta nuevamente")

        elif opcion == "2":
            print("\n--- Registrar Usuario ---")
            ident = input("Identificación: ")
            nombre = input("Nombre completo: ")
            correo = input("Correo electrónico: ")
            usuario = Usuario(ident, nombre, correo)
            restaurante.agregar_usuario(usuario)

        elif opcion == "3":
            restaurante.listar_productos()

        elif opcion == "4":
            restaurante.listar_usuarios()

        elif opcion == "5":
            print("\n--- Realizar Venta ---")
            try:
                id_p = int(input("ID del producto a vender: "))
                usuario_id = input("Identificación del usuario: ")
                cant = int(input("Cantidad: "))
                restaurante.vender_producto(id_p, usuario_id, cant)
            except ValueError:
                print("❌ Datos inválidos")

        elif opcion == "6":
            print("\n--- Consultar Ventas ---")
            usuario_id = input("Identificación del usuario: ")
            restaurante.consultar_ventas_usuario(usuario_id)

        elif opcion == "7":
            print("👋 ¡Gracias por usar el sistema!")
            break

        else:
            print("❌ Opción no válida, intenta del 1 al 7")


if __name__ == "__main__":
    main()