import os
os.system(' cls')

soma = 0
for i in range(4):
    nota= float(input(' Digite sua nota: '))

    soma= soma + nota

media = soma / 4


print(f' A média é: {media}')