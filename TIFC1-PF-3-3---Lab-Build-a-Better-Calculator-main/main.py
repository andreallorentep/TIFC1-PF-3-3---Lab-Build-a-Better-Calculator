def addmultiplenumbers(numbers):
    # Devuelve la suma de todos los números en la lista
    return sum(numbers)


def multiplymultiplenumbers(numbers):
    # Devuelve el producto de todos los números en la lista
    resultado = 1
    for n in numbers:
        resultado *= n
    return resultado


def isitaninteger(num):
    # Comprueba si el número es un entero (por ejemplo, 3.0 cuenta como entero)
    return num == int(num)


def isiteven(num):
    # Comprueba si el número es un entero par
    return isitaninteger(num) and int(num) % 2 == 0


def main():
    print("Calculadora simple")
    print("Introduce números separados por espacios:")

    numbers = list(map(float, input().split()))

    print("\nElige una operación:")
    print("1 - Sumar")
    print("2 - Multiplicar")
    print("3 - Comprobar si el primer número es par")
    print("4 - Comprobar si el primer número es un entero")

    choice = input("Introduce tu opción: ")

    if choice == "1":
        print("Resultado:", addmultiplenumbers(numbers))
    elif choice == "2":
        print("Resultado:", multiplymultiplenumbers(numbers))
    elif choice == "3":
        print("Resultado:", isiteven(numbers[0]))
    elif choice == "4":
        print("Resultado:", isitaninteger(numbers[0]))
    else:
        print("Opción no válida")


if __name__ == "__main__":
    main()