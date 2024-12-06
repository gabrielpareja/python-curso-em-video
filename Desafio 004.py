#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele
algo = input('Digite algo: ')
print ('O tipo primitivo disso é : ',type(algo))
print ('Só espaços? ',algo.isspace())
print ('É número? ',algo.isnumeric())
print ('É alfabético? ',algo.isalpha())
print ('Está em minúsculo? ',algo.islower())
print ('Está em maiúsculo? ',algo.isupper())
print ('Está capitalizada? ',algo.istitle())