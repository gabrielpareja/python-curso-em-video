#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Resolver de forma matemática
n = int(input('Digite um número de 0 a 9999 para ser analizado em unidade, dezena, centena e unidade: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('=====Analisando o numero=====')
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
print('=============================')