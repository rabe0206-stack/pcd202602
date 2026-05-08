
# Sistema de Inventario Modular

## Descripción
Este proyecto en Python procesa un archivo CSV de inventario de una tienda de tecnología. El programa lee el archivo `data/inventario.csv`, valida cada registro, detecta qué productos necesitan reorden y genera un reporte en `outputs/reporte_inventario.csv`.

Un producto necesita reorden cuando su **stock actual es menor que su stock mínimo**.

## Estructura del proyecto
```text
reto-semana-04/
├── main.py
├── README.md
├── .gitignore
├── models/
│   ├── __init__.py
│   └── producto.py
├── utils/
│   ├── __init__.py
│   ├── io.py
│   └── validators.py
├── data/
│   └── inventario.csv
└── outputs/
    └── reporte_inventario.csv
```

## Funcionalidades
El sistema realiza las siguientes tareas:

1. Lee un archivo CSV con información del inventario.
2. Valida los datos de cada producto.
3. Ignora registros inválidos sin detener la ejecución.
4. Identifica los productos que requieren reorden.
5. Ordena los productos por unidades faltantes, de mayor a menor.
6. Genera un archivo CSV con el reporte final.

## Campos de entrada
El archivo `data/inventario.csv` debe contener las siguientes columnas:

- `sku`
- `nombre`
- `categoria`
- `precio`
- `stock`
- `stock_minimo`

Ejemplo:

```csv
sku,nombre,categoria,precio,stock,stock_minimo
SKU001,Laptop HP,Electronica,15000,5,10
SKU002,Mouse Logitech,Accesorios,500,20,10
SKU003,Teclado Mecanico,Accesorios,1200,3,8
```

## Validaciones
El sistema valida que:

- el SKU no esté vacío
- el nombre no esté vacío
- la categoría no esté vacía
- el precio sea numérico y mayor o igual a 0
- el stock sea entero y mayor o igual a 0
- el stock mínimo sea entero y mayor o igual a 0

Si una fila tiene errores, el programa la ignora y continúa con las demás.

## Archivo de salida
El programa genera el archivo:

```text
outputs/reporte_inventario.csv
```

Este archivo contiene únicamente los productos que necesitan reorden, con las columnas:

- `sku`
- `nombre`
- `categoria`
- `stock_actual`
- `stock_minimo`
- `unidades_faltantes`
- `valor_inventario`

## Regla de reorden
Un producto entra al reporte cuando:

```python
stock < stock_minimo
```

Las unidades faltantes se calculan así:

```python
stock_minimo - stock
```

El valor del inventario se calcula así:

```python
precio * stock
```

## Cómo ejecutar el proyecto
Desde la terminal, dentro de la carpeta del proyecto, ejecutar:

```bash
python3 main.py
```

## Ejemplo de salida en consola
```bash
Leyendo inventario...
Fila 9965 inválida: Precio inválido: INVALIDO
Fila 9984 inválida: Stock inválido: None
Fila 9999 inválida: Precio inválido: None
Se cargaron 8907 productos válidos.
Productos que necesitan reorden: 3492
Reporte generado correctamente en: outputs/reporte_inventario.csv
Proceso terminado.
```

## Tecnologías utilizadas
- Python 3
- Módulo estándar `csv`

## Autor
Sebastian Ramirez  
Instituto Politécnico Nacional
````
