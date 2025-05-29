#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
    else:
        print(f'O número {n} já foi adicionado! Tente outro número.')
    end = str(input('Deseja adicionar mais elementos? (S/N) ')).upper()
    if end == 'N':
        break
lista.sort()
print('A lista com todos os números que você adicionou é: ',end ='')
print(lista)

