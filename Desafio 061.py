#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
a11 = a1 + (10 * r)
termo = a1
while termo < a11:
    print(f'{termo} ', end='')
    print(f'➔ ' if termo < a11 else '=', end='')
    termo += r
print('FIM')