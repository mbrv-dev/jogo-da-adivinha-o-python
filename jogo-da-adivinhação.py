#Sistema de Advinhação

import random

print('--------------------------------')
print('🎯 Jogo da Adivinhação 🎯')
print('🎯 Tente descobrir o número entre 1 e 100 🎯')
print('--------------------------------')

numero_secreto = random.randint(1, 100)
contador = 0

while True:
    try:
        contador += 1
        tentativa = int(input('Digite um numero: '))
        if tentativa == numero_secreto:
            print('-----------------------')
            print('Parabens, Você Acertou!')
            break
        elif tentativa > numero_secreto:
            print('Muito Alto')
        elif tentativa < numero_secreto:
            print('Muito Baixo')
    except ValueError:
        print('Valor invalido, Digite um numero!')

print(f'Com {contador} tentativas')
print(f'O numero secreto era {numero_secreto}')
print('-----------------------')

