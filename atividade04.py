'''Faça um script para receber um número qualquer e informar na tela se é par ou ímpar'''

def verificar_paridade(num):
    if num % 2 == 0:
        return 'Par'
        
    else:
        return 'Ímpar'
    

while True:
    num = int(input(f'Digite um número: '))

    if num == 0:
        break
    else: 
        resultado = verificar_paridade(num)
    print(f'Seu número é {resultado}')