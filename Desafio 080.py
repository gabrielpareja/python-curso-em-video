#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista. No final, mostre a lista ordenada na tela.
lista = []
for c in range(0,5):
    n = int(input('Digite um número: '))
    lista.append(n)
lista.sort()
print(lista)
