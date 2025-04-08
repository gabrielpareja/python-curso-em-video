#Desenvolva um programa que leia 6 numeros interiros e mostre a soma apenas daqueles que forem pares
#Se o valor digitado for impar desconsidere-o.
import random, time
lista = list(range(1 , 10000))
lista2 = random.sample(lista, 6)
pares = [num for num in lista2 if num % 2 == 0]
print(f'A lista de 6 números aleatórios entre 1 e 10000 é: {lista2}')
print(f'A lista de números pares entre 0 e 10000 selecionados aleatóriamente é: {pares}')
print(f'A soma entre os números pares é: {sum(pares)}')

