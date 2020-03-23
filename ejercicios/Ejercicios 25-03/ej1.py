import sys

numero = int(input("Ingrese un numero mayor a cero: "))

if numero <= 0:
    print("ERROR.")
    sys.exit()

numero_lista = ''
lista = []
i = 0

while(i < 3):
    numero_lista += str(numero)
    lista.append(int(numero_lista))
    i += 1
    print(lista[-1])
    print("-------")

resultado = 0
for i in range(0, 3):
    resultado += lista[i]

print("\nEl resultado es: ", resultado)
