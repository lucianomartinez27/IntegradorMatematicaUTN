def multiplicar_binarios(binario1, binario2):
    resultados = []
    contador = 0
    for bit in reversed(binario2):
        if bit == "1":
            resultado = binario1 + "0" * contador
            resultados.append(resultado)
        contador += 1
    total = "0"
    for resultado in resultados:
        total = sumar_binarios(resultado, total)
    return total

def sumar_binarios():
    a = input("Ingresá el primer número binario: ")
    b = input("Ingresá el segundo número binario: ")
    resultado = bin(int(a, 2) + int(b, 2))[2:]
    print(f"La suma es: {resultado}")

def restar_binarios():
    a = input("Ingresá el primer número binario: ")
    b = input("Ingresá el segundo número binario: ")
    resultado = bin(int(a, 2) - int(b, 2))[2:]
    print(f"La resta es: {resultado}")

def operacionSumaResta():
    a = input("Primer número binario: ")
    b = input("Segundo número binario: ")

    suma = bin(int(a, 2) + int(b, 2))[2:]
    resta = bin(int(a, 2) - int(b, 2))[2:]

    print(f"Suma: {suma}")
    print(f"Resta: {resta}")


operacionSumaResta()