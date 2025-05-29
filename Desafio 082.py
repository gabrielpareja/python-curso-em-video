#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas
lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um número (0 para encerrar): '))
    lista.append(n)
    if n == 0:
        break
    elif n % 2 != 0:
        impares.append(n)
    else:
        pares.append(n)
lista.sort() , pares.sort() , impares.sort()
print(f'A lista ficou : {lista}')
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')
