#Faça um programa que leia a largura e a altura de uma parede em metros , calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
b = float(input('Qual a base da parede? '))
h = float(input('Qual a altura da parede? '))
area = (b*h)
l = (area/2)
print(f'A área da parede é {area} e precisará de {l} litros para pintá-la')