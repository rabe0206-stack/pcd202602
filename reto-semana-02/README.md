# Reto Semana 2: Clasificador de Temperaturas

## Descripción
Este programa lee un archivo CSV desde stdin, convierte todas las temperaturas a Celsius, clasifica cada ciudad según su clima y escribe un reporte estandarizado en stdout.

## Archivos del proyecto
- `main.py`: programa principal
- `README.md`: documentación
- `.gitignore`: archivos ignorados por git
- `tests/`: archivos de prueba

## Cómo funciona
El programa:
1. Lee un CSV con columnas: `ciudad,temperatura,unidad`
2. Convierte temperaturas en Fahrenheit a Celsius
3. Clasifica cada temperatura
4. Ignora líneas inválidas
5. Imprime un nuevo CSV como salida

## Clasificación
- `< 0` → Congelante
- `0 a 15` → Frio
- `16 a 25` → Templado
- `26 a 35` → Calido
- `> 35` → Extremo

## Ejecución

### Linux / Mac
```bash
python3 main.py < tests/entrada1.txt

 
 ## Ejemplo de entrada
ciudad,temperatura,unidad
CDMX,22,C
Nueva York,50,F
Moscu,-10,C
Miami,95,F
Cancun,30,C
Chicago,14,F

##Ejemplo de salida
ciudad,temperatura_celsius,clasificacion
CDMX,22.0,Templado
Nueva York,10.0,Frio
Moscu,-10.0,Congelante
Miami,35.0,Calido
Cancun,30.0,Calido
Chicago,-10.0,Congelante


Guarda con `Ctrl + S`.

---

## 5. Abrir `.gitignore`

En el panel izquierdo:
- busca `.gitignore`
- doble clic

Si no lo ves, revisa que no estén ocultos los archivos con punto.

Pega esto:

```gitignore
__pycache__/
*.pyc
.vscode/

## Manejo de líneas inválidas
El programa ignora líneas que:
- no tengan exactamente 3 columnas
- tengan una temperatura no numérica
- tengan una unidad distinta de `C` o `F`

## Autor
Sebastian Ramirez