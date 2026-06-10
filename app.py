from calculator import sumar, restar, multiplicar, dividir

def menu():
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")
    print("____________________________")

def main():
    while True:
        menu()
        option = input("Selecciona una opción: ")
        if option == "1":
            numero1 = float(input("Ingresa el primer número: "))
            numero2 = float(input("Ingresa el segundo número: "))
            resultado = sumar(numero1, numero2)
            print("El resultado es: " + str(resultado))
        elif option == "2":
            numero1 = float(input("Ingresa el primer número: "))
            numero2 = float(input("Ingresa el segundo número: "))
            resultado = restar(numero1, numero2)
            print("El resultado es: " + str(resultado))
        elif option == "3":
            numero1 = float(input("Ingresa el primer número: "))
            numero2 = float(input("Ingresa el segundo número: "))
            resultado = multiplicar(numero1, numero2)
            print("El resultado es: " + str(resultado))
        elif option == "4":
            numero1 = float(input("Ingresa el primer número: "))
            numero2 = float(input("Ingresa el segundo número: "))
            resultado = dividir(numero1, numero2)
            print("El resultado es: " + str(resultado))
        elif option == "0":
            print("Salir")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()