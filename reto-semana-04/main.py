from utils.io import leer_inventario, escribir_reporte


def main():
    ruta_entrada = "data/inventario.csv"
    ruta_salida = "outputs/reporte_inventario.csv"

    print("Leyendo inventario...")
    productos = leer_inventario(ruta_entrada)

    print(f"Se cargaron {len(productos)} productos válidos.")

    productos_reorden = []
    for producto in productos:
        if producto.necesita_reorden():
            productos_reorden.append(producto)

    productos_reorden.sort(
        key=lambda producto: producto.calcular_unidades_faltantes(),
        reverse=True
    )

    print(f"Productos que necesitan reorden: {len(productos_reorden)}")

    escribir_reporte(ruta_salida, productos_reorden)
    print("Proceso terminado.")


if __name__ == "__main__":
    main()