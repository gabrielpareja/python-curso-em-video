#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
import time
n1 = int(input('Digite o primeiro número : '))
n2 = int(input('Digite o segundo número :'))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('Qual a sua opção? : '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}!')
        time.sleep(2)
    elif opção == 2:
        multiplicar = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {multiplicar}!')
        time.sleep(2)
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior número entre {n1} e {n2} é {maior}!')
        time.sleep(2)
    elif opção == 4:
        n1 = int(input('Digite um novo primeiro número : '))
        n2 = int(input('Digite um novo segundo número : '))
print('-----Fim do programa-----')
