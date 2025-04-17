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
        print("ERROR, opción inválida. Debe elegir 'D' o 'B'")
    continuar = input("¿Querés seguir? (s/n): ")
    if continuar.lower() != "s":
        break 