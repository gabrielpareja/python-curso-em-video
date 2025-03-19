#Crie um programa que lleia um número interiro e mostre na tela se ele é PAR ou Impar.
n = int(input('Digite um número para ver se ele é par ou não : '))
if n % 2 == 1:
    print('O número {} é ímpar!'.format(n))
else:
    print('O número {} é par!'.format(n))