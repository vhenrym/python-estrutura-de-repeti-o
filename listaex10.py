alunos = int(input('Digite a quantidade de alunos: '))
notas = int(input('Quantas notas são? '))
for i in range(alunos):
    soma = 0
    for n in range (notas):
        nota = int(input('Coloque a nota dos alunos: '))
        soma += nota

    media = soma / notas
    print(f'a média das notas são: {media}')