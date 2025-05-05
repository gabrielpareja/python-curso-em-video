#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
print('~' * 30)
print('SUPERMERDADO GABRIEL BOLADÃO')
print('~' * 30)
cont1000 = 0
soma = 0
menor = 0
cont = 0
while True:
    produto = str(input('Qual o produto que você deseja comprar? '))
    valor = int(input('QUal o valor do produto? R$ '))
    simnao = str(input('Deseja adicionar mais produtos na lista? [S/N] ')).strip().upper()
    soma += valor
    cont += 1
    if valor > 1000:
        cont1000 += 1
    elif simnao == 'N':
        break
    elif cont == 1 or valor < menor:
        menor = valor
print('~' * 30)
print(f'O total gasto na compra foi de R${soma},00.')
print(f'{cont1000} produtos foram acima de R$1000,00!')
print(f'O produto mais barato custa o valor de R${menor}')
