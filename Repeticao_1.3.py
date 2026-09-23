import os
import time
os.system('cls')


numero = int(input('Digite seu número: '))
for i in range(numero,0,-1):
    print(i)
    time.sleep(1)

print ('E FIM')