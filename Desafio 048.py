#Faca um programa que calcule a soma entre todos os numeros impares que sao multiplos de 3 e que esteja entre 1 e 500
#Para ser multiplo, a divisao deve ser inteira
total = 0
for n in range(1 , 501 , 2):
    if n % 3 == 0:
        total += n
print('A soma de todos os multiplos de 3 entre 0 e 500 e {}!'.format(total))