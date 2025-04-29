#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final mostre:
#A media de idade do grupo
#Qual e o nome do homem mais velho
#Quantas mulheres tem menos de 20 anos
nomemaisvelho = ''
idademaisvelho = 0
mediaidade = 0
somaidade = 0
totmulher20 = 0
for p in range(1,5):
    print(f'---------{p}ª Pessoa--------')
    nome = str(input('Qual o nome da pessoa: ')).strip()
    idade = int(input('Qual a idade da pessoa: '))
    sexo = str(input('Qual o sexo (M/F): ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'M':
        idademaisvelho = idade
        nomemaisvelho = nome
    if sexo in 'M' and idade > idademaisvelho:
        idademaisvelho = idade
        nomemaisvelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('----------------------------------------')
print(f'A média das idades do grupo é {mediaidade}!')
print(f'O nome do homem mais velho é {nomemaisvelho} e ele tem {idademaisvelho}!')
print(f'E a quantidade de mulheres com menos de 20 anos é {totmulher20}! ')

