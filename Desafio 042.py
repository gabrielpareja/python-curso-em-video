#Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes.
l1 = int(input('Diga o primeiro lado:'))
l2 = int(input('Diga o segundo lado:'))
l3 = int(input('Diga o terceiro lado:'))
if ((l1+l2)>l3 and (l2+l3)>l1 and (l3+l1)>l2):
    print('Com esses lados é possível ter um triângulo!')
    elif l1 == l2 and l2 == l3 and l3 == l1:
        print('Esse triângulo é isósceles!')
    elif l1 == l2 == l3:
        print('Esse triânglo é Equilátero!')
else:
    print('Com esses lados não é possível formar um triângulo!')