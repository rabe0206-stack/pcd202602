# Reto Semana 1: Calculadora de Sumas

## Descripción
Este proyecto resuelve el reto de la Semana 1 de la materia **Programación para Ciencia de Datos** del **Instituto Politécnico Nacional (IPN)**.

El objetivo del programa es leer líneas de datos desde la **entrada estándar (stdin)**, limpiar los valores eliminando caracteres inválidos, truncar números decimales a enteros y calcular la suma de los valores de cada línea.

El programa está diseñado para ser robusto, ya que puede manejar:

- líneas vacías  
- números con decimales  
- caracteres basura dentro de los números  
- espacios extra  
- valores faltantes entre comas  

Por cada línea de entrada, el programa imprime una línea con el resultado correspondiente.

---

# Autor

Sebastian Ramirez  
Instituto Politécnico Nacional  
Programación para Ciencia de Datos  
Semestre Febrero – Julio 2026

---

# Cómo ejecutar el programa

El programa se ejecuta desde la terminal utilizando **entrada estándar (stdin)**.

### Linux / Ubuntu / Mac

```bash
python3 main.py < tests/prueba.txt
```

o

```bash
cat tests/prueba.txt | python3 main.py
```

### Windows PowerShell

```powershell
Get-Content tests/prueba.txt | python main.py
```

### Windows CMD

```cmd
type tests\prueba.txt | python main.py
```

---

# Ejemplo de entrada

Archivo de entrada:

```txt
1,2,3
10

1.9,2.1,3.7
1a2,3b,4
-5,10,3
  5 , 10 , 15
```

---

# Ejemplo de salida

```txt
6
10
0
6
19
8
30
```

---

# Funcionamiento del programa

El programa sigue el siguiente proceso:

1. Lee cada línea desde **stdin**.
2. Verifica si la línea está vacía.
3. Divide la línea usando **comas** como separador.
4. Limpia cada valor eliminando caracteres inválidos.
5. Convierte los valores a números.
6. Trunca los decimales usando `int()`.
7. Suma todos los valores de la línea.
8. Imprime el resultado.

---

# Estructura del proyecto

```
reto-semana-01/
├── main.py
├── README.md
├── .gitignore
└── tests/
    └── prueba.txt
```

Descripción de archivos:

- **main.py**  
Contiene la implementación del programa que procesa las líneas de entrada.

- **README.md**  
Documentación del proyecto y explicación de uso.

- **.gitignore**  
Archivos que Git debe ignorar.

- **tests/prueba.txt**  
Archivo de prueba para verificar el funcionamiento del programa.

---

# Pruebas

Para probar el programa se puede utilizar el archivo:

```
tests/prueba.txt
```

Ejecutando:

```bash
python3 main.py < tests/prueba.txt
```

El programa imprimirá la suma correspondiente a cada línea del archivo.

---

# Notas

El programa maneja correctamente varios casos especiales, por ejemplo:

- líneas vacías
- valores con letras mezcladas
- espacios antes o después de los números
- valores vacíos entre comas
- números decimales truncados a enteros

Esto permite que el programa funcione incluso cuando los datos de entrada están "sucios".
