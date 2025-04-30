#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = int(input('Digite um número: '))
soma = n
cont = 0
while n != 999:
    n = int(input('Digite outro número para ser somado: (digite 999 para parar) '))
    soma += n
    cont += 1
print(f'A soma dos {cont} números é {soma - 999}!')
