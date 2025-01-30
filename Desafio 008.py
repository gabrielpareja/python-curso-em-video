#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = int(input('Diga quantos metros deseja converter:'))
cm = (m*100)
mm = (m*1000)
print(f'Em {m} metros há {cm} centímetros e {mm} milímetros')