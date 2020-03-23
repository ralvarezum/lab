lista = []

while True:
    try:
        numero = int(input("\nIngrese un numero mayor o igual a cero: "))
        if(numero < 0):
            raise ValueError
        lista.append(numero)
    except ValueError:
        print("\nERROR. Debe ingresar un numero mayor o igual a cero!")
 
    carga = input("\nFinalizar el ingreso de numeros? S/s: ")
    if(carga == 'S' or carga == 's'):
        break
    else:
        print("\nCargando...")

print("\nHISTOGRAMA\n")
for i in lista:
    for j in range(i):
        print('o', end='')
    print()
