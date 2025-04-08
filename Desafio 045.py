#Crie um programa que faça o computador jogar Jokenpô com você.
import random
lista = ['pedra' , 'papel' , 'tesoura']
print('=-=-=-=-=-=-=-= Vamos jogar pedra, papel e tesoura! =-=-=-=-=-=-=-=')
print('[1]- Pedra\n[2]- Papel\n[3]- Tesoura')
jogada = str(input('O que você irá escolher? '))
if jogada == '1':
    jogada = 'pedra'
elif jogada == '2':
    jogada = 'papel'
elif jogada == '3':
    jogada = 'tesoura'
computador = random.choice(lista)
print('*JO\n*KEN\n*PO!')
print('Eu joguei {}!'.format(computador))
print('Voce jogou {}!'.format(jogada))
if computador == jogada:
    print('Jogamos a mesma coisa, deu empate!')
elif computador != jogada:
    if jogada == 'pedra' and computador == 'papel':
       print('Eu ganhei hahaha!')
    elif jogada == 'pedra' and computador == 'tesoura':
        print('Droga, eu perdi!')
    elif jogada == 'papel' and computador == 'pedra':
        print('Droga eu perdi!')
    elif jogada == 'papel' and computador == 'tesoura':
        print('Eu ganhei hahaha!')
    elif jogada == 'tesoura' and computador == 'papel':
        print('Droga eu perdi!')
    elif jogada == 'tesoura' and computador == 'pedra':
        print('Eu ganhei hahaha!')

