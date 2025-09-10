from textlib import reverse, count_vowels, is_palindrome, to_upper, concat

def menu():
    while True:
        print("\n=== TextLib Demo ===")
        print("1. Invertir texto")
        print("2. Contar vocales")
        print("3. Verificar palíndromo")
        print("4. Convertir a mayúsculas")
        print("5. Concatenar dos cadenas")
        print("0. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            s = input("Ingresa el texto: ")
            print("Resultado:", reverse(s))

        elif opcion == "2":
            s = input("Ingresa el texto: ")
            print("Número de vocales:", count_vowels(s))

        elif opcion == "3":
            s = input("Ingresa el texto: ")
            print("¿Es palíndromo?:", is_palindrome(s))

        elif opcion == "4":
            s = input("Ingresa el texto: ")
            print("En mayúsculas:", to_upper(s))

        elif opcion == "5":
            a = input("Cadena A: ")
            b = input("Cadena B: ")
            print("Concatenado:", concat(a, b))

        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()

