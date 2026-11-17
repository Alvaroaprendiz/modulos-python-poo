class Pedido:
    def __init__(self, cliente, producto, cantidad, precio_unitario):
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def total(self):
        return self.cantidad * self.precio_unitario

    def resumen(self):
        return (f"Pedido de {self.cliente}: {self.cantidad} x {self.producto} "
                f"a ${self.precio_unitario:.2f} c/u = ${self.total():.2f}")
