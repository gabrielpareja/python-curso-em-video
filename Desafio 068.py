#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
cont = 0
while True:
    n = int(input('Digite um valor entre 0 e 10: '))
    pi = str(input('Par ou impar: ')).strip().upper()
    comp = randint(0,11)
    tot = n + comp
    print(f'Você escolheu {n} e o computador {comp}, a soma deu {tot}.')
    if tot % 2 != 0:
        print(f'O valor total de {tot} é ímpar!')
        if pi == 'I':
            print('Você venceu!')
            print('~' * 30)
            cont += 1
        else:
            print('~' * 30)
            print('Você perdeu! Tente na próxima!')
            break
    else:
        print(f'O valor total de {tot} é par!')
        if pi == 'P':
            print('Você venceu!')
            print('~' * 30)
            cont += 1
        else:
            print('~' * 30)
            print('Você perdeu! Tente na próxima!')
            break
print('~' * 30)
print(f'Você jogou {cont} vezes contra o computador até perder!')
print('~' * 30)
