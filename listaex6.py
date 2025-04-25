numero = int(input("Numero: "))

maior = numero
menor = numero

for n in range(9):
    numero = int(input("Numero: "))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

        print(f'Maior: {maior}')
        print(f'Menor: {menor}')