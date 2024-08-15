'''Faça um script que leia N números. Finalizar quando digitar 0. No final mostrar o total de números digitados, o total de números ímpares e o total de números pares.'''

total = 0
total_par = 0
total_impar = 0

while True:
    num = int(input('Digite um número: '))
    if num == 0:
        break
    if num % 2 == 0:
        total_par += 1
    else: 
        total_impar += 1
    total += 1
    
print(f'O total de números digitados é {total}, o total de ímpares é {total_impar} e o total de pares é {total_par}')
