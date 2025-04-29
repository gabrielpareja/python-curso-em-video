#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
lista = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
comp = random.choice(lista)
print('~~~~~~~~ Estoou pensando em um número de 0 a 10, tente adivinhar! ~~~~~~~~')
n = int(input('Digite o número : '))
while n != comp :
    n = int(input('Você errou! Digite outro número: '))
print(f'Parabéns você acertou! O número é {comp}!')
