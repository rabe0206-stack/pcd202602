import sys

def limpiar_valor(valor):
    valor = valor.strip()
    caracteres_validos = "0123456789.-"
    resultado = ""

    for char in valor:
        if char in caracteres_validos:
            resultado += char

    return resultado


def convertir_a_entero(texto):
    if texto == "":
        return 0

    try:
        numero = float(texto)
        return int(numero)
    except ValueError:
        return 0


def procesar_linea(linea):
    if linea.strip() == "":
        return 0

    valores = linea.strip().split(",")
    suma = 0

    for valor in valores:
        valor_limpio = limpiar_valor(valor)
        numero = convertir_a_entero(valor_limpio)
        suma += numero

    return suma


def main():
    for linea in sys.stdin:
        resultado = procesar_linea(linea)
        print(resultado)


if __name__ == "__main__":
    main()
