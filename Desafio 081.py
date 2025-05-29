#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:                                                                                                                                              A) Quantos números foram digitados.                                                                 B) A lista de valores, ordenada de forma decrescente.                                                               C) Se o valor 5 foi digitado e está ou não na lista.
quantidade = 0
lista = []
while True:
    n = int(input('Digite um valor (Digite 0 para encerrar): '))
    if n == 0:
        break
    else:
        lista.append(n)
        quantidade += 1
lista.sort(reverse=True)
print(f'Você digitou {quantidade} números.')
print(f'A lista de forma ordenada é: {lista}')
if 5 in lista:
    print(f'O número 5 aparece na lista!')
else:
    print('O número 5 não aparece na lista!')