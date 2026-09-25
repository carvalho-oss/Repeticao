import os
os.system('cls')

print('ACUMULANDO VALORES EM UMA VARÍAVEL.')
soma = 0

for i in range(3):

    soma += int(input(' Digite seu numero para somar: '))

print(f'\nVALOR FINAL DA VARÍAVEL soma:{soma}')

