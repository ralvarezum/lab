import sys

numero = int(input("Ingrese un numero mayor a cero: "))
numero2 = int(input("Ingrese un numero para indicar la cantidad de sumas: "))

numero_lista = ''
lista = []
i = 0

if numero <= 0:
    print("ERROR.")
    sys.exit()

while(i < numero2):
    numero_lista += str(numero)
    lista.append(int(numero_lista))
    i += 1
    print(lista[-1])
    print("-------")

resultado = 0
for i in range(0, numero2):
    resultado += lista[i]

print("\nEl resultado es: ", resultado)
