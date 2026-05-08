# Reto Semana 3: Analizador de Ventas

## Programación para Ciencia de Datos
**Instituto Politécnico Nacional**  
Semestre Febrero-Julio 2026

---

## Descripción del proyecto

Este proyecto consiste en desarrollar un programa en Python que funciona como un **analizador de ventas** para una tienda de tecnología. El programa recibe como entrada un archivo en formato **CSV** a través de la entrada estándar (`stdin`), procesa las transacciones de venta y genera un **reporte consolidado por producto**.

El reporte final muestra, para cada producto, cuántas unidades se vendieron, cuál fue el ingreso total generado y cuál fue el precio promedio de venta. Además, la salida aparece **ordenada de mayor a menor según el ingreso total**, para identificar primero los productos más rentables.

---

## Objetivo

Aplicar conceptos fundamentales de Python utilizados en ciencia de datos, especialmente lectura de datos, procesamiento de texto, uso de diccionarios, agrupación de información, cálculo de métricas, ordenamiento de datos, manejo de errores y generación de salida en formato CSV.

---

## Problema planteado

En una tienda de tecnología se registran múltiples transacciones de venta cada día. Cada transacción contiene la fecha, el nombre del producto, la cantidad vendida y el precio unitario. El objetivo del programa es agrupar todas las transacciones por producto y calcular un resumen consolidado.

Si un mismo producto aparece en varias filas del archivo de entrada, todas esas transacciones deben sumarse en una sola fila del reporte final.

---

## Formato de entrada

El programa recibe un archivo CSV con el siguiente formato:

- La primera línea contiene los encabezados: `fecha,producto,cantidad,precio_unitario`
- Las siguientes líneas contienen una transacción por línea

### Ejemplo de entrada

```csv
fecha,producto,cantidad,precio_unitario
2026-01-01,Laptop,2,15000.00
2026-01-02,Mouse,10,250.00
2026-01-03,Laptop,1,14500.00
2026-01-04,Teclado,5,800.00
2026-01-05,Mouse,8,250.00
```

---

## Formato de salida

El programa imprime un archivo CSV con el siguiente formato:

- Encabezado: `producto,unidades_vendidas,ingreso_total,precio_promedio`
- Una línea por producto
- Ordenado de mayor a menor por `ingreso_total`

### Ejemplo de salida

```csv
producto,unidades_vendidas,ingreso_total,precio_promedio
Laptop,3,44500.00,14833.33
Mouse,18,4500.00,250.00
Teclado,5,4000.00,800.00
```

---

## Reglas de procesamiento

El programa debe cumplir con las siguientes reglas:

### 1. Agrupar por producto
Todas las transacciones del mismo producto deben consolidarse en una sola fila.

### 2. Calcular métricas por producto
Para cada producto se deben calcular:

- **unidades_vendidas**: suma de todas las cantidades vendidas
- **ingreso_total**: suma de `(cantidad × precio_unitario)` en todas las transacciones
- **precio_promedio**: `ingreso_total / unidades_vendidas`

### 3. Ordenar por ingreso total descendente
El reporte debe estar ordenado de mayor a menor ingreso total.

### 4. Formato correcto de números
- `unidades_vendidas` debe imprimirse como entero
- `ingreso_total` debe tener 2 decimales
- `precio_promedio` debe tener 2 decimales

### 5. Ignorar líneas inválidas
Si una línea tiene menos de 4 columnas, tiene una cantidad no numérica o tiene un precio no numérico, entonces esa línea debe ignorarse completamente.

---

## Explicación de la solución

La solución se basa en el uso de un **diccionario** para agrupar la información por producto. Cada producto se usa como clave dentro de un diccionario, y como valor se almacenan sus acumulados: unidades vendidas e ingreso total.

Por ejemplo:

```python
productos = {
    "Laptop": {
        "unidades_vendidas": 3,
        "ingreso_total": 44500.00
    },
    "Mouse": {
        "unidades_vendidas": 18,
        "ingreso_total": 4500.00
    }
}
```

Después de agrupar, se calcula el precio promedio para cada producto y finalmente se ordenan los resultados por ingreso total.

---

## Lógica del programa

El programa sigue estos pasos:

1. Leer las líneas del archivo.
2. Ignorar el encabezado.
3. Ignorar líneas vacías.
4. Separar cada línea usando comas.
5. Validar que la línea tenga exactamente 4 columnas.
6. Intentar convertir `cantidad` a entero y `precio_unitario` a decimal.
7. Si la conversión falla, ignorar la línea.
8. Si el producto no existe en el diccionario, crearlo.
9. Acumular unidades e ingreso total.
10. Calcular el precio promedio por producto.
11. Ordenar los productos por ingreso total en orden descendente.
12. Imprimir la salida en formato CSV.

---

## Código principal

```python
import sys


def leer_y_agrupar_ventas():
    productos = {}
    primera_linea = True

    for linea in sys.stdin:
        linea = linea.strip()

        if not linea:
            continue

        if primera_linea:
            primera_linea = False
            continue

        partes = linea.split(',')

        if len(partes) != 4:
            continue

        producto = partes[1]

        try:
            cantidad = int(partes[2])
            precio_unitario = float(partes[3])
        except ValueError:
            continue

        if producto not in productos:
            productos[producto] = {
                "unidades_vendidas": 0,
                "ingreso_total": 0.0
            }

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
```

---

## Ejemplo de funcionamiento

### Entrada

```txt
fecha,producto,cantidad,precio_unitario
2026-01-01,Laptop,2,15000.00
2026-01-02,Mouse,10,250.00
2026-01-03,Laptop,1,14500.00
2026-01-04,Teclado,5,800.00
2026-01-05,Mouse,8,250.00
```

### Salida

```txt
producto,unidades_vendidas,ingreso_total,precio_promedio
Laptop,3,44500.00,14833.33
Mouse,18,4500.00,250.00
Teclado,5,4000.00,800.00
```

---

## Conceptos aplicados

En este proyecto se aplican los siguientes temas:

- Variables
- Tipos de datos
- Lectura de archivos
- Ciclos `for`
- Condicionales
- Diccionarios
- Diccionarios anidados
- Manejo de excepciones
- Listas
- Ordenamiento con `sorted()`
- Funciones
- Formato de salida con `f-strings`

---

## Conclusión

Este proyecto permite practicar una situación muy parecida a una tarea real de análisis de datos: leer información, limpiarla, agruparla, calcular métricas relevantes y producir un reporte ordenado.

La solución implementada en Python cumple con los requerimientos del reto: agrupa por producto, calcula unidades vendidas, calcula ingreso total, calcula precio promedio, ordena por ingreso descendente e ignora datos inválidos.