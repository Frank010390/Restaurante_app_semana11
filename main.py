from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n" + "="*60)
    print("      SISTEMA DE GESTIÓN DE RESTAURANTE - SEMANA 12")
    print("="*60)
    print("1. Registrar producto")
    print("2. Registrar usuario")
    print("3. Listar productos")
    print("4. Realizar venta")
    print("5. Consultar ventas de un usuario")
    print("6. Salir")
    print("-"*60)

def main():
    app = Restaurante()
    print("✅ Sistema iniciado. Datos cargados desde archivos JSON.")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Registrar Producto ---")
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            try:
                precio = float(input("Precio: "))
                stock = int(input("Stock inicial: "))
            except ValueError:
                print("❌ Error: Precio y stock deben ser números")
                continue

            ok, msg = app.registrar_producto(codigo, nombre, precio, stock)
            print("✅" if ok else "❌", msg)

        elif opcion == "2":
            print("\n--- Registrar Usuario ---")
            identificacion = input("Identificación: ")
            nombre = input("Nombre completo: ")
            correo = input("Correo electrónico: ")

            ok, msg = app.registrar_usuario(identificacion, nombre, correo)
            print("✅" if ok else "❌", msg)

        elif opcion == "3":
            print("\n--- Lista de Productos ---")
            productos = app.listar_productos()
            if not productos:
                print("No hay productos registrados")
                continue
            for p in productos:
                print(f"[{p.codigo}] {p.nombre} | Precio: ${p.precio:.2f} | Stock: {p.stock}")

        elif opcion == "4":
            print("\n--- Realizar Venta ---")
            id_usuario = input("Identificación del usuario: ")
            codigo_prod = input("Código del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
            except ValueError:
                print("❌ Error: La cantidad debe ser un número entero")
                continue

            ok, msg = app.realizar_venta(id_usuario, codigo_prod, cantidad)
            print("✅" if ok else "❌", msg)

        elif opcion == "5":
            print("\n--- Ventas de Usuario ---")
            id_usuario = input("Identificación del usuario: ")
            ventas = app.consultar_ventas_por_usuario(id_usuario)

            if not ventas:
                print("No se encontraron ventas para ese usuario")
                continue

            usuario = app.buscar_usuario_por_identificacion(id_usuario)
            nombre_usuario = usuario.nombre if usuario else "Usuario desconocido"
            print(f"\nCompras de: {nombre_usuario}")
            print("-"*50)
            total_general = 0
            for v in ventas:
                prod = app.buscar_producto_por_codigo(v.codigo_producto)
                nombre_prod = prod.nombre if prod else "Producto desconocido"
                precio = prod.precio if prod else 0
                subtotal = precio * v.cantidad
                total_general += subtotal
                print(f"[{v.id_venta}] {v.fecha} | {nombre_prod} × {v.cantidad} = ${subtotal:.2f}")
            print("-"*50)
            print(f"TOTAL: ${total_general:.2f}")

        elif opcion == "6":
            print("\n👋 Saliendo del sistema... ¡Hasta luego!")
            break

        else:
            print("❌ Opción no válida. Intente nuevamente")

if __name__ == "__main__":
    main()