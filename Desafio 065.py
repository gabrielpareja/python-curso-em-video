#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resp = 'S'
soma = n = media = cont = maior = menor = 0
n2 = n
while resp in 'Ss':
    n2 = int(input('Digite um número : '))
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    soma += n2
    cont += 1
    media = soma / cont
    if cont == 1:
        maior = menor = n2
    else:
        if n2 > maior:
            maior = n2
        if n2 < menor:
            menor = n2
print(f'O maior número é {maior} e o menor número é {menor}!')
print(f'A soma de {cont} números deu {soma} e a média dos valores é {media}!')

