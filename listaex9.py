num = int(input('Digite um numero: '))
fatorial = 1

for i in range(1, num+1):
    fatorial = fatorial * i
print(f'o fatorial do numero {num} é: {fatorial}')