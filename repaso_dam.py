asignaturas = [
{"nombre": "Programacion", "nota": 8.5, "aprobado": True},
{"nombre": "Base de Datos", "nota": 4.0, "aprobado": False},
{"nombre": "Sistemas Informaticos", "nota": 7.0, "aprobado": True},
{"nombre": "Entornos de Desarrollo", "nota": 9.0, "aprobado": True}
]


def contar_aprobados(lista):
    return sum(1 for asignatura in lista if asignatura["aprobado"])



def nota_media(lista):
    if not lista:
        return 0
    return sum(asignatura["nota"] for asignatura in lista) / len(lista)


def nota_superior_a(lista, umbral):
    return [asignatura for asignatura in lista if asignatura["nota"] > umbral]


print(f"Cantidad de asignaturas aprobadas: {contar_aprobados(asignaturas)}")
print(f"Nota media: {nota_media(asignaturas):.2f}")
print(f"Asignaturas con nota superior a 7.0: {len(nota_superior_a(asignaturas, 7.0))}")