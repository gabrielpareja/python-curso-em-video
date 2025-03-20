#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais
n = int(input('Digite o primeiro número a ser analisado: '))
n2= int(input('Digite o segundo número a ser analisado: '))
if n > n2:
    print('O primeiro valor é maior!')
elif n2 > n:
    print('O segundo valor é maior!')
elif n == n2:
    print('Não existe valor maior, os dois são iguais!')