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