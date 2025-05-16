#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
n = ( randint(1,10) , randint(1,10) , randint(1,10) , randint(1,10) ,randint(1,10))
print(f'Os itens são {n}')
maior = sorted(n)[4]
menor = sorted(n)[0]
print(f'O menor termo é {menor} e o maior é {maior}.')