"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

palavra = input('Informe uma palavra: ')
palavra_invertida = []
palavra_final = ''
contador = len(palavra)
while contador > 0: 
    palavra_invertida += palavra[contador-1]
    contador -= 1

for letra in palavra_invertida:
    palavra_final += letra

print('A palavra invertida em string é:', palavra_final)
