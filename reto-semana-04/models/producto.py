class Producto:
    def __init__(self, sku, nombre, categoria, precio, stock, stock_minimo):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)
        self.stock = int(stock)
        self.stock_minimo = int(stock_minimo)

    def necesita_reorden(self):
        return self.stock < self.stock_minimo

    def calcular_unidades_faltantes(self):
        if self.necesita_reorden():
            return self.stock_minimo - self.stock
        return 0

    def calcular_valor_inventario(self):
        return self.precio * self.stock

    def __str__(self):
        return (
            f"{self.nombre} ({self.sku}) - "
            f"Categoría: {self.categoria}, "
            f"Precio: ${self.precio:.2f}, "
            f"Stock: {self.stock}, "
            f"Stock mínimo: {self.stock_minimo}"
        )

    def __repr__(self):
        return (
            f"Producto(sku='{self.sku}', nombre='{self.nombre}', "
            f"categoria='{self.categoria}', precio={self.precio}, "
            f"stock={self.stock}, stock_minimo={self.stock_minimo})"
        )