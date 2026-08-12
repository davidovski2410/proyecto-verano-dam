clientes = [
    {"id": 1, "nombre": "Laura", "empresa": "TechCorp", "facturacion": 12000, "activo": True},
    {"id": 2, "nombre": "Carlos", "empresa": "DevStudio", "facturacion": 8500, "activo": False},
    {"id": 3, "nombre": "Ana", "empresa": "InnovaSoft", "facturacion": 20000, "activo": True}
]

def obtener_clientes_activos(lista):
    return [c for c in lista if c["activo"]]

def calcular_facturacion_promedio(lista):
    if not lista:
        return 0
    total = sum(c["facturacion"] for c in lista)
    return total / len(lista)

print("--- CLIENTES ACTIVOS ---")
for cliente in obtener_clientes_activos(clientes):
    print(f"- {cliente['nombre']} ({cliente['empresa']}): {cliente['facturacion']}€")

promedio = calcular_facturacion_promedio(clientes)
print(f"\nFacturación promedio: {promedio:.2f}€")