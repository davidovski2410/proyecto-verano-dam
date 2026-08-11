# Registro de productos (Estructura habitual en SGE / Odoo)
productos = [
    {"nombre": "Portatil", "precio": 800, "stock": 5},
    {"nombre": "Raton", "precio": 20, "stock": 15}
]

def calcular_total(lista):
    total = sum(p["precio"] * p["stock"] for p in lista)
    return total

print(f"Valor total del inventario: {calcular_total(productos)} euros")