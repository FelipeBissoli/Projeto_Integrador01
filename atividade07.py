'''Ler 10 números inteiros e imprimir quantos são pares e quantos são ímpares.'''
pares = 0
impares = 0

for i in range (5):
    num = int(input('Digite um número: '))

    if num % 2 == 0:
        pares = pares + 1
    
    else:
        impares = impares + 1

print(f'Você digitou {pares} números pares',end='\n'f'Você digitou {impares} números impares')



