#Escreva um programa que faça o computador "Pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
#escolhido pelo computador
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
n = [0 , 1 , 2 , 3 , 4 , 5]
a = (random.choices(n))
print('Estou pensando em um número... Tente adivinhar qual é (hehehe)... ')
r = int(input('Digite o número que você tentou adivinhar : '))
if r == a:
   print('Parabéns, você acertou! O número é {}'.format(a))
else:
   print('Infelizmente você errou!O número era {}, e não {}! Tente novamente depois palindromo.'.format(a,r))
   
