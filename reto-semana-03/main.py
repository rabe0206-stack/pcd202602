import sys


def leer_y_agrupar_ventas():
    productos = {}
    primera_linea = True

    for linea in sys.stdin:
        linea = linea.strip()

        # Saltar líneas vacías
        if not linea:
            continue

        # Saltar encabezado
        if primera_linea:
            primera_linea = False
            continue

        partes = linea.split(',')

        # Validar que tenga 4 columnas
        if len(partes) != 4:
            continue

        fecha = partes[0]
        producto = partes[1]

        # Validar y convertir cantidad y precio
        try:
            cantidad = int(partes[2])
            precio_unitario = float(partes[3])
        except ValueError:
            continue

        # Crear producto si no existe
        if producto not in productos:
            productos[producto] = {
                "unidades_vendidas": 0,
                "ingreso_total": 0.0
            }

        # Acumular datos
        productos[producto]["unidades_vendidas"] += cantidad
        productos[producto]["ingreso_total"] += cantidad * precio_unitario

    return productos


def calcular_reporte(productos):
    reporte = []

    for producto, datos in productos.items():
        unidades = datos["unidades_vendidas"]
        ingreso = datos["ingreso_total"]
        precio_promedio = ingreso / unidades if unidades > 0 else 0.0

        reporte.append({
            "producto": producto,
            "unidades_vendidas": unidades,
            "ingreso_total": ingreso,
            "precio_promedio": precio_promedio
        })

    return reporte


def ordenar_reporte(reporte):
    return sorted(reporte, key=lambda x: x["ingreso_total"], reverse=True)


def imprimir_csv(reporte):
    print("producto,unidades_vendidas,ingreso_total,precio_promedio")
    for fila in reporte:
        print(
            f"{fila['producto']},"
            f"{fila['unidades_vendidas']},"
            f"{fila['ingreso_total']:.2f},"
            f"{fila['precio_promedio']:.2f}"
        )


def main():
    productos = leer_y_agrupar_ventas()
    reporte = calcular_reporte(productos)
    reporte_ordenado = ordenar_reporte(reporte)
    imprimir_csv(reporte_ordenado)


if __name__ == "__main__":
    main()