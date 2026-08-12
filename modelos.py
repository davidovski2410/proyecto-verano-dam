class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def hay_stock(self):
        return self.stock > 0

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)

# Prueba de la clase
p1 = Producto("Teclado Mecánico", 50.0, 10)
print(f"Producto: {p1.nombre} | Precio inicial: {p1.precio}€")

p1.aplicar_descuento(10) # 10% de descuento
print(f"Precio con 10% descuento: {p1.precio}€")
print(f"¿Hay stock disponible?: {p1.hay_stock()}")