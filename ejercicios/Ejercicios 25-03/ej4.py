lista = []
archivo = open("histograma.txt", "r")

for linea in archivo.readlines():
    if len(linea) > 0 and linea != '\n':
        lista.append(int(linea))

print("\nHISTOGRAMA\n")
for i in lista:
    for j in range(i):
        print('o', end='')
    print()
