#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
#Lembrando que a hipotenusa²=CO²xCA²
import math
co = float(input('Qual o cateto oposto? '))
ca = float(input('Qual o cateto adjatente? '))
co2 = math.pow(co,2)
ca2 = math.pow(ca,2)
h = co2 + ca2
h2 = math.sqrt(h)
print(f'O triângulo tem cateto oposto de {co} e cateto adjacente {ca}.')
print(f'Sua hipotenusa é {h2}.')
#No caso há uma função que calcula a hipotenusa direto chamada "hypot"