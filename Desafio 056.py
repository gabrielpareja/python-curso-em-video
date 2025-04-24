#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final mostre:
#A media de idade do grupo
#Qual e o nome do homem mais velho
#Quantas mulheres tem menos de 20 anos
homemvelho = ""
idadehv = 0
somaidades = 0
mulheresmenos20 = 0
for i in range(1,5):
    print(f'Pessoa {i}:')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').upper().strip()

