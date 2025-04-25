#Solicitar a idade de 10 pessoas e calcular a média das idades

soma = 0

n = int(input("Quantidade de pessoas: "))
for cont in range(n):
    idade = int(input('Informe a idade: '))
    soma += idade

media = soma / n
print(f'Média das idades: {media}')