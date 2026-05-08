# Perfilador de Datasets

Herramienta que analiza archivos CSV y genera reportes de calidad de datos automáticamente.

## Requisitos

- Python 3.8 o superior

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/usuario/reto-semana-05.git
cd reto-semana-05
```

### 2. Crear ambiente virtual
```bash
python3 -m venv .venv
```

### 3. Activar ambiente virtual
```bash
# Linux/Mac
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

## Uso

```bash
python main.py --input <archivo_entrada.csv> --output <archivo_salida.csv>
```

También puedes usar las formas cortas `-i` y `-o`:
```bash
python main.py -i data/ventas.csv -o outputs/perfil_ventas.csv
```

### Ejemplos

```bash
python main.py --input data/ventas.csv    --output outputs/perfil_ventas.csv
python main.py --input data/empleados.csv --output outputs/perfil_empleados.csv
python main.py --input data/sensores.csv  --output outputs/perfil_sensores.csv
```

## Formato de Salida

El perfil generado es un CSV con una fila por cada columna del archivo original:

| Columna            | Descripción                                      |
|--------------------|--------------------------------------------------|
| nombre_columna     | Nombre de la columna analizada                   |
| tipo_inferido      | Tipo detectado: numerico / texto / fecha / booleano |
| total_registros    | Total de filas (sin encabezado)                  |
| valores_nulos      | Cantidad de celdas vacías                        |
| porcentaje_nulos   | Porcentaje de nulos (2 decimales)                |
| valores_unicos     | Cantidad de valores distintos (sin nulos)        |
| porcentaje_unicos  | Porcentaje de unicidad (2 decimales)             |
| ejemplo_valor      | Primer valor no nulo encontrado                  |

### Ejemplo de salida para `ventas.csv`

```
nombre_columna,tipo_inferido,total_registros,valores_nulos,porcentaje_nulos,valores_unicos,porcentaje_unicos,ejemplo_valor
fecha,fecha,5,0,0.00,5,100.00,2026-01-01
producto,texto,5,0,0.00,4,80.00,Laptop
cantidad,numerico,5,1,20.00,4,80.00,2
precio,numerico,5,1,20.00,3,60.00,15000.00
vendedor,texto,5,1,20.00,3,60.00,Ana
```

## Reglas de detección

- **Nulo**: celda vacía, solo espacios o `None`. El string `"0"`, `"null"` o `"None"` NO son nulos.
- **Tipo**: se infiere si más del 80% de los valores no nulos corresponden a ese tipo.
- **Únicos**: se cuentan solo valores no nulos, con distinción entre mayúsculas y minúsculas.

## Autor

Sebastian Ramirez Becerril - Febrero 2026  
Instituto Politécnico Nacional — Programación para Ciencia de Datos