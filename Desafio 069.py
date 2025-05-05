#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
cont18 = conth = contm20 = 0
print('~~' * 30)
print('CADASTRE UMA PESSOA')
print('~~' * 30)
while True:
    idade = int(input('Idade : '))
    if idade > 18:
        cont18 += 1
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if sexo == 'M':
        conth += 1
    elif sexo == 'F' and idade < 20:
        contm20 += 1
    print('-' * 30)
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()
    print('-' * 30)
    if continuar == 'N':
        break
print(f'A quantidade de pessoas maiores de 18 anos é {cont18}!')
print(f'A quantidade de homens é {conth}!')
print(f'A quantidade de mulheres acima de 20 anos é {contm20}!')

