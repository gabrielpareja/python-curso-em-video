#Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:0 – 1 – 1 – 2 – 3 – 5 – 8
#A Sequência de Fibonacci é uma famosa sequência numérica onde cada número é a soma dos dois anteriores
print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)
t1 = 0
t2 = 1
n = int(input('Quantos termos você quer mostrar? '))
cont = 3
print(f'{t1} ➔ {t2} ➔ ',end='')
while cont <= n:
    t3 = t1 + t2
    print(f'{t3} ➔ ',end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')


    
    
