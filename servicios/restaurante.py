from .archivo_servicio import ArchivoServicio
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from datetime import datetime

class Restaurante:
    def __init__(self):
        self.archivo = ArchivoServicio()

        # 📋 Listas PRINCIPALES (se mantienen para guardar y listar)
        self.productos = []
        self.usuarios = []
        self.ventas = []

        # ⚡ ÍNDICES para búsquedas RÁPIDAS
        self.productos_por_codigo = {}
        self.usuarios_por_id = {}
        self.ventas_por_usuario = {}
        self.codigos_existentes = set()
        self.ids_usuarios_existentes = set()

        self._cargar_datos()
        self._construir_indices()

    def _cargar_datos(self):
        self.productos = self.archivo.cargar_json("productos.json", Producto)
        self.usuarios = self.archivo.cargar_json("usuarios.json", Usuario)
        self.ventas = self.archivo.cargar_json("ventas.json", Venta)

    def _construir_indices(self):
        """Reconstruir índices al iniciar el programa"""
        self.productos_por_codigo.clear()
        self.usuarios_por_id.clear()
        self.ventas_por_usuario.clear()
        self.codigos_existentes.clear()
        self.ids_usuarios_existentes.clear()

        for prod in self.productos:
            self.productos_por_codigo[prod.codigo] = prod
            self.codigos_existentes.add(prod.codigo)

        for usu in self.usuarios:
            self.usuarios_por_id[usu.identificacion] = usu
            self.ids_usuarios_existentes.add(usu.identificacion)

        for ven in self.ventas:
            if ven.identificacion_usuario not in self.ventas_por_usuario:
                self.ventas_por_usuario[ven.identificacion_usuario] = []
            self.ventas_por_usuario[ven.identificacion_usuario].append(ven)

    def _guardar_todo(self):
        self.archivo.guardar_json("productos.json", self.productos)
        self.archivo.guardar_json("usuarios.json", self.usuarios)
        self.archivo.guardar_json("ventas.json", self.ventas)

    # ========== PRODUCTOS ==========
    def registrar_producto(self, codigo, nombre, precio, stock):
        if codigo in self.codigos_existentes:
            return False, f"El producto con código {codigo} ya existe"
        nuevo = Producto(codigo, nombre, precio, stock)
        self.productos.append(nuevo)
        self.productos_por_codigo[codigo] = nuevo
        self.codigos_existentes.add(codigo)
        self._guardar_todo()
        return True, "Producto registrado correctamente"

    def buscar_producto_por_codigo(self, codigo):
        return self.productos_por_codigo.get(codigo)

    def listar_productos(self):
        return self.productos

    # ========== USUARIOS ==========
    def registrar_usuario(self, identificacion, nombre, correo):
        if identificacion in self.ids_usuarios_existentes:
            return False, f"El usuario con identificación {identificacion} ya existe"
        nuevo = Usuario(identificacion, nombre, correo)
        self.usuarios.append(nuevo)
        self.usuarios_por_id[identificacion] = nuevo
        self.ids_usuarios_existentes.add(identificacion)
        self._guardar_todo()
        return True, "Usuario registrado correctamente"

    def buscar_usuario_por_identificacion(self, identificacion):
        return self.usuarios_por_id.get(identificacion)

    def listar_usuarios(self):
        return self.usuarios

    # ========== VENTAS ==========
    def realizar_venta(self, identificacion_usuario, codigo_producto, cantidad):
        usuario = self.buscar_usuario_por_identificacion(identificacion_usuario)
        producto = self.buscar_producto_por_codigo(codigo_producto)

        if not usuario:
            return False, "Usuario no encontrado"
        if not producto:
            return False, "Producto no encontrado"
        if producto.stock < cantidad:
            return False, f"Stock insuficiente. Disponible: {producto.stock}"

        producto.stock -= cantidad
        id_venta = f"V{len(self.ventas)+1:04d}"
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        nueva_venta = Venta(id_venta, identificacion_usuario, codigo_producto, cantidad, fecha_actual)
        self.ventas.append(nueva_venta)

        if identificacion_usuario not in self.ventas_por_usuario:
            self.ventas_por_usuario[identificacion_usuario] = []
        self.ventas_por_usuario[identificacion_usuario].append(nueva_venta)

        self._guardar_todo()
        return True, f"Venta registrada. Total: ${producto.precio * cantidad:.2f}"

    def consultar_ventas_por_usuario(self, identificacion_usuario):
        return self.ventas_por_usuario.get(identificacion_usuario, [])