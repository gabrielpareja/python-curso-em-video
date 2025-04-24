#Crie um programa que leia uma frase qualquer e diga se ela e um palindromo. Desconsiderando os espacos.
frase = str(input('Digite uma frase: ')).replace(" " , "").lower()
invertida = frase[::-1]
print(f'A frase normal é : {frase}')
print(f'A frase invertida é: {invertida}')
if frase == invertida:
    print('Sua frase é um palíndromo!')
else:
    print('Sua frase não é um palíndromo!')
