#Crie um programa que leia uim número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math
num = float(input('Digite um número para arrendondá-lo: '))
a = math.trunc(num)
print(f'eu número inteiro é: {a}')