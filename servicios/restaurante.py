from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:
    def __init__(self):
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []
        self.archivo = ArchivoServicio()

    # ─────────────── CARGA DE DATOS ───────────────
    def cargar_datos(self):
        self._productos = self.archivo.cargar_productos()
        self._usuarios = self.archivo.cargar_usuarios()
        self._ventas = self.archivo.cargar_ventas()
        print(f"✅ Productos: {len(self._productos)} | Usuarios: {len(self._usuarios)} | Ventas: {len(self._ventas)}")

    # ─────────────── PRODUCTOS ───────────────
    def agregar_producto(self, producto: Producto):
        self._productos.append(producto)
        self.archivo.guardar_productos(self._productos)
        print(f"✅ Producto '{producto.nombre}' registrado")

    def listar_productos(self):
        if not self._productos:
            print("📋 Sin productos registrados")
            return
        print("\n════════════ LISTA DE PRODUCTOS ════════════")
        for p in self._productos:
            print(p)
        print("═" * 46)

    def buscar_producto(self, id_producto: int):
        for p in self._productos:
            if p.id_producto == id_producto:
                return p
        return None

    # ─────────────── USUARIOS ───────────────
    def agregar_usuario(self, usuario: Usuario):
        self._usuarios.append(usuario)
        self.archivo.guardar_usuarios(self._usuarios)
        print(f"✅ Usuario '{usuario.nombre}' registrado")

    def listar_usuarios(self):
        if not self._usuarios:
            print("📋 Sin usuarios registrados")
            return
        print("\n════════════ LISTA DE USUARIOS ════════════")
        for u in self._usuarios:
            print(u)
        print("═" * 46)

    def buscar_usuario(self, identificacion: str):
        for u in self._usuarios:
            if u.identificacion == identificacion:
                return u
        return None

    # ─────────────── VENTAS ───────────────
    def vender_producto(self, id_producto: int, usuario_id: str, cantidad: int) -> bool:
        usuario = self.buscar_usuario(usuario_id)
        producto = self.buscar_producto(id_producto)

        if usuario is None:
            print("❌ Usuario no encontrado")
            return False
        if producto is None:
            print("❌ Producto no encontrado")
            return False
        if cantidad <= 0:
            print("❌ La cantidad debe ser mayor a cero")
            return False
        if producto.stock < cantidad:
            print(f"❌ Stock insuficiente. Disponible: {producto.stock}")
            return False

        # ✅ Todo válido → registrar venta
        venta = Venta(usuario_id, id_producto, cantidad)
        self._ventas.append(venta)
        producto.vender(cantidad)

        # 💾 Guardar cambios
        self.archivo.guardar_ventas(self._ventas)
        self.archivo.guardar_productos(self._productos)
        print(f"✅ Venta realizada → {producto.nombre} × {cantidad}")
        return True

    def consultar_ventas_usuario(self, usuario_id: str):
        ventas_usuario: list[Venta] = []
        for v in self._ventas:
            if v.usuario_id == usuario_id:
                ventas_usuario.append(v)

        if not ventas_usuario:
            print(f"📋 El usuario {usuario_id} no tiene ventas registradas")
            return []

        print(f"\n═════════ VENTAS DEL USUARIO {usuario_id} ═════════")
        for v in ventas_usuario:
            prod = self.buscar_producto(int(v.producto_codigo))
            nombre_prod = prod.nombre if prod else f"Producto {v.producto_codigo}"
            print(f"• {nombre_prod} | Cantidad: {v.cantidad}")
        print("═" * 52)
        return ventas_usuario