#//////////////////// SUMA Y RESTA ///////////////////////////

def sumar_binarios(a, b):
    resultado = bin(int(a, 2) + int(b, 2))[2:]
    print(f"La suma es: {resultado}")
    return resultado

def restar_binarios(a, b):
    diferencia = int(a, 2) - int(b, 2)
    if diferencia >= 0:
        resultado = bin(diferencia)[2:] 
    else:
        resultado = '-' + bin(abs(diferencia))[2:] 
    print(f"La resta es: {resultado}")
    return resultado

def operacionSumaResta():
    # inputs suma
    a = input("Primer número binario: ")
    b = input("Segundo número binario: ")
    
    suma = sumar_binarios(a, b)
    resta = restar_binarios(a, b)
operacionSumaResta()


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

#////////////////////////////////////////////////////////////////

def dividir():
    # division de numeros binarios

    # Pido dos numeros binarios como str
    num_bin1 = input('Ingrese un numero decimal: ')
    num_bin2 = input('Ingrese otro numero decimal: ')

    # Convierto de binario a decimal
    num_dec1 = int(num_bin1, 2) # Pongo el ,2 para indicar que el numero que estamos pasando esta en base 2, osea binario.
    num_dec2 = int(num_bin2, 2)

    # Hago un if para evitar la división por cero
    if num_dec2 == 0:
        print('No se puede dividir por 0, intente con otro  numero')

    # Hago la division de los numeros decimales
    resultado_dec = num_dec1 // num_dec2 

    # Vuelvo a convertir el resultado de vuelta a binario
    resultado_bin = bin(resultado_dec)[2:] # Pongo el [2:] para que omita los dos primeros caracteres del prefijo
    print(f'La divison binaria entre {num_bin1} y {num_bin2} es: {resultado_bin}')





#////////////////////////////////////////////////////////////////
def convertir_binario():
    while True:
        opcion = input("Elija la opción D para Decimal a Binario, o B para Binario a Decimal: ")
        if opcion.lower() == "d":
            try:
                numero = int(input("Ingresa un numero decimal: "))
                binario = bin(numero)[2:]
                print(f"La conversión a binario es {binario}")
            except ValueError:
                print("ERROR, ingrese un número decimal válido")

        elif opcion.lower() == "b":
            numero = input("Ingrese un número binario: ")
            if all(char in "01" for char in numero):
                decimal = int(numero, 2)
                print(f"La conversión a decimal es: {decimal}")
            else:
                print("ERROR, eso no es un número binario")
        else: 
            print("ERROR, INGRESE UNA OPCION VALIDA")
        continuar = input("si desea continuar presione 's', de no ser asi presione 'n': ")
        if continuar.lower() == "s":
            continue
        elif continuar.lower() == "n":
            break
        else:
            print("ERROR, INGRESE 's' PARA CONTINUAR O 'n' PARA SALIR.")