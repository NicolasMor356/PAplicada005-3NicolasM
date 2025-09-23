import os

try:
    while True:
        # pide el número al usuario
        num = input("Ingresa un número: ")
        
        # limpia la consola
        os.system("cls" if os.name == "nt" else "clear")
        
        # convertir a entero
        try:
            num = int(float(num))  # solo acepta enteros o decimales
        except ValueError:
            print("Entrada inválida, escribe un número.")
            continue
        
        # recorrer del 1 hasta la variable num
        for i in range(1, num+1):
            if i % 2 == 0:
                print(f"{i} es par")
            else:
                print(f"{i} es impar")

except KeyboardInterrupt:
    print("\nPrograma detenido por el usuario.")
