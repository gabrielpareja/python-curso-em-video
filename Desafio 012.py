#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
#Lembrando que ex: 20% de desconto sobre algo(valor x vezes 0,8)
p = float(input('Qual o preço do produto?\n'))
d = p * 0.95
print(f'O produto com 5% de desconto fica {round(d,2)}')