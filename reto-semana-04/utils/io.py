import csv
from models.producto import Producto
from utils.validators import validar_producto


def leer_inventario(ruta_archivo):
    productos = []

    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            columnas_esperadas = [
                "sku",
                "nombre",
                "categoria",
                "precio",
                "stock",
                "stock_minimo"
            ]

            if lector.fieldnames != columnas_esperadas:
                print("Advertencia: Las columnas del archivo no coinciden exactamente con las esperadas.")
                print(f"Columnas encontradas: {lector.fieldnames}")

            for numero_fila, fila in enumerate(lector, start=2):
                try:
                    sku = fila["sku"]
                    nombre = fila["nombre"]
                    categoria = fila["categoria"]
                    precio = fila["precio"]
                    stock = fila["stock"]
                    stock_minimo = fila["stock_minimo"]

                    es_valido, error = validar_producto(
                        sku, nombre, categoria, precio, stock, stock_minimo
                    )

                    if not es_valido:
                        print(f"Fila {numero_fila} inválida: {error}")
                        continue

                    producto = Producto(
                        sku, nombre, categoria, precio, stock, stock_minimo
                    )
                    productos.append(producto)

                except KeyError as e:
                    print(f"Fila {numero_fila} inválida: falta la columna {e}")
                except Exception as e:
                    print(f"Error procesando fila {numero_fila}: {e}")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

    return productos


def escribir_reporte(ruta_archivo, productos_reorden):
    try:
        with open(ruta_archivo, mode="w", newline="", encoding="utf-8") as archivo:
            campos = [
                "sku",
                "nombre",
                "categoria",
                "stock_actual",
                "stock_minimo",
                "unidades_faltantes",
                "valor_inventario"
            ]

            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()

            for producto in productos_reorden:
                escritor.writerow({
                    "sku": producto.sku,
                    "nombre": producto.nombre,
                    "categoria": producto.categoria,
                    "stock_actual": producto.stock,
                    "stock_minimo": producto.stock_minimo,
                    "unidades_faltantes": producto.calcular_unidades_faltantes(),
                    "valor_inventario": f"{producto.calcular_valor_inventario():.2f}"
                })

        print(f"Reporte generado correctamente en: {ruta_archivo}")

    except Exception as e:
        print(f"Error al escribir el reporte: {e}")