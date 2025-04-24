#Faca um programa que leia o peso de 5 pessoas. No final,mostre qual foi o menor e o maior peso lidos.
lista = []
for peso in range(1,6):
    pesos = int(input(f'Digite o peso da {peso}º pessoa: '))
    lista.append(pesos)
print(f'O maior peso foi {max(lista)}.')
print(f'O menor peso foi {min(lista)}.')