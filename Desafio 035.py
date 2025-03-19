#Desenvolva um programa que leia o comprimnento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.
#A condição de existência de um triângulo é que a soma de 2 lados tem que ser maior que o terceiro lado.
l1 = int(input('Diga o primeiro lado:'))
l2 = int(input('Diga o segundo lado:'))
l3 = int(input('Diga o terceiro lado:'))
if ((l1+l2)>l3 and (l2+l3)>l1 and (l3+l1)>l2):
    print('Com esses lados é possível ter um triângulo!')
else:
    print('Com esses lados não é possível formar um triângulo!')