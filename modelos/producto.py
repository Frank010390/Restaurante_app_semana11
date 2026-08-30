class Producto:
    def __init__(self, id_producto: int, nombre: str, precio: float, categoria: str,
                 stock: int = 0, disponible: bool = True):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        self.disponible = disponible

    def vender(self, cantidad: int) -> bool:
        if cantidad > 0 and self.stock >= cantidad:
            self.stock -= cantidad
            return True
        return False

    def a_diccionario(self) -> dict:
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria,
            "stock": self.stock,
            "disponible": self.disponible
        }

    def __str__(self) -> str:
        estado = "✅ Disponible" if self.disponible and self.stock > 0 else "❌ Agotado"
        return f"ID: {self.id_producto} | {self.nombre} | ${self.precio:.2f} | Stock: {self.stock} | {self.categoria} | {estado}"