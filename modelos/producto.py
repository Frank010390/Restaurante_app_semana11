class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int = 0):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        if self.stock < 0:
            raise ValueError("El stock no puede ser negativo")

    def vender(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a cero")
        if self.stock < cantidad:
            raise ValueError("Stock insuficiente")
        self.stock -= cantidad

    def convertir_a_diccionario(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def reconstruir_desde_diccionario(cls, datos: dict):
        return cls(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            precio=datos["precio"],
            stock=datos["stock"]
        )