#Desafio 50 feito de outra forma
soma = 0
count = 0
for c in range(1,7):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        soma += num
        count += 1
print('Você informou {} numeros pares e a soma deles é {}!'.format(count,soma))