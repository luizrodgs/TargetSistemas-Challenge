"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""

def fibonacci(numero, limite):
    contador = 1
    limite = limite
    penultimo_numero = 0
    ultimo_numero = 1
    achou = False
    while achou==False:
        if contador > 1000:
            print('A sequência extrapolou o limite imposto e não encontrou o termo buscado')
            break
        elif ultimo_numero == numero:
            print('O número informado está na sequência!')
            achou = True
        else:
            novo_numero = ultimo_numero + penultimo_numero
            penultimo_numero = ultimo_numero
            ultimo_numero = novo_numero
            print(novo_numero)
            contador += 1

numero = int(input('Informe o número a conferir na sequência: '))
limite = int(input('Informe o número para limite de termos na sequência: '))

fibonacci(numero, limite)
