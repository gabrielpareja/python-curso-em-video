#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
for c in range(1,6):
    lista.append(int(input(f'Digite o {c}º valor: ')))
lista.sort()
print(f'O menor valor da lista é {lista[0]}, e o maior é {lista[4]}.')
