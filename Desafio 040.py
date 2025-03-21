#Crie um programa que leia duas notas de um aluno e calcule sua média , mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaioxo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: Aprovado
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2
if m < 5.0:
    print('Você ficou reprovado com a média de {:.1f}!'.format(m))
elif 5.0 < m < 6.9:
    print('Você está de recuperação com a média de {:.1f}!'.format(m))
elif m > 7.0:
    print('Parabéns você está aprovado com a média de {:.1f}!'.format(m))
