#Crie um programa que faça o computador jogar Jokenpô com você.
import random
lista = ['pedra' , 'papel' , 'tesoura']
print('Vamos jogar pedra, papel e tesoura!')
jogada = str(input('O que você irá escolher? '))
computador = random.choice(lista)
print('Eu joguei {}!'.format(computador))
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
else:
    print('Mas o que é isso rapaz?')

