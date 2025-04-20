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

def alinear(divisor, dividento):
    if divisor



# Division de numeros binarios

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




