import os
os.system('cls')

# CONSTANTE.
QUANTIDADE_REPETICOES = 5
pares = 0
ímpares = 0

for i in range(QUANTIDADE_REPETICOES):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        pares = pares + 1
        pares+= 1

    else:
        ímpares = ímpares + 1

print(f'Quantidade de pares: {pares}')
print(f'Quantidade de ímpares: {ímpares}')

print('FIM')