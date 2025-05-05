#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1,11):
        tot = c * n
        print(f'{c} x {n} = {tot}')
    print('-' * 30)
    print('Digite um valor negativo para encerrar o programa')
print('Fim do programa')
print('-' * 30)