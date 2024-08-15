'''Imprimir todos os números de 1 até 100'''
for i in range (1,101):
    print(i, end=' ')

    if i % 10 == 0:
        print(end='\n')