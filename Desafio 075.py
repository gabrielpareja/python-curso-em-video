#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
tupla = (int(input('Digite um número: ')) , (int(input('Digite um segundo número: '))) , (int(input('Digite um terceiro número: '))) , (int(input('Digite um último número: '))))
print('~' * 30)
print(tupla)
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O número 3 aparece na {tupla.index(3)} posição.')
else:
    print('O valor 3 não aparece na lista de números')
print('Os valores pares digitados foram: ', end= '')
for n in tupla:
    if n % 2 == 0:
        print(n , end='')
