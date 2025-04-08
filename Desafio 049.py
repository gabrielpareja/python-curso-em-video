#Refaca o desafio 9 de um numero que o usuario escolher, so que agora utilizando um laco 'For'
#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('Digite um numero para fazer a tabuada: '))
print(f'Tabuado do numero {n}: ')
for t in range(11):
    resultado = n * t
    print(f'{n} x {t} = {resultado}')
