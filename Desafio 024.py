#024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
n = str(input('Digite algum nome para ser analisado : '))
print('O nome {} começa com "SANTO"? '.format(n))
print("Santo" in n[:5])